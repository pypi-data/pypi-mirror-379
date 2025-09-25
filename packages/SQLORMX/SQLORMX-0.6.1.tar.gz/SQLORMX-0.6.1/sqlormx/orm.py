import sys
from datetime import datetime
from enum import Enum, IntEnum
from functools import lru_cache
from typing import Sequence, Union, List, Tuple, Any
from sqlexecutorx.conf import lru_cache_size

from .snowflake import get_snowflake_id
from .support import DBError, NotFoundError
from . import log_support, orm_support, db
from .constant import NO_LIMIT, DEFAULT_KEY_FIELD, KEY, SELECT_KEY, TABLE, UPDATE_BY, UPDATE_TIME, DEL_FLAG, \
    KEY_STRATEGY, KEY_SEQ


class DelFlag(IntEnum):
    UN_DELETE = 0
    DELETED = 1


class KeyStrategy(Enum):
    """
    SNOWFLAKE: 由Snowflake算法生成主键
    DB_AUTO_INCREMENT: 由数据库的AUTO_INCREMENT自动生成主键

    在Windows上，使用Snowflake可能会报下列错误，这是因为Snowflake生成的id是15位的数字，而Windows上C语言的long类型是32位的
    OverflowError: Python int too large to convert to C long

    如果用的是mysql.connector，且在Windows上开发测试，可以就在初始化数据库的时候加上参数'use_pure'为True用纯python的connect; 在linux是部署生成环境时去掉'use_pure'用
    C语言写的connect, 以提高性能.
    """
    SNOWFLAKE = 'snowflake'
    DB_AUTO_INCREMENT = 'db_auto_increment'


class Model:
    """
    Create a class extends Model:

    from sqlormx import Model, db
    from dataclasses import dataclass
    
    @dataclass
    class Person(Model):
        __table__ = 'person'
        id: int = None
        name: str = None
        age: int = None

    then you can use like follow:
        db.init(person='xxx', password='xxx', database='xxx', host='xxx', ...)  # or db.init(...) init db first,
        person = Person(name='张三', age=55)
        effect_rowcount = person.persist()
        id = person.inst_save()
    """
    
    __key__ = DEFAULT_KEY_FIELD
    __del_flag__ = 'del_flag'
    __update_by__ = 'update_by'
    __update_time__ = 'update_time'
    __key_strategy__ = KeyStrategy.DB_AUTO_INCREMENT

    def __str__(self):
        return str({k: v for k, v in self.__dict__.items() if not k.startswith("__")})

    def __getattr__(self, name):
        if KEY == name:
            return self._get_key()
        elif TABLE == name:
            return self.get_table()
        elif UPDATE_BY == name:
            return self._get_update_by_field()
        elif UPDATE_TIME == name:
            return self._get_update_time_field()
        else:
            return None

    def persist(self, *fields, ignored_none=True) -> int:
        """
        person = Person(name='张三', age=55)
        effect_rowcount = person.persist()
        :return: effect rowcount
        """
        log_support.orm_inst_log('persist', self.__class__.__name__)
        kv = self._get_kv(ignored_none, None, *fields)
        return self.insert(**kv)

    def inst_save(self, *fields, ignored_none=True) -> Any:
        """
        person = Person(name='张三', age=55)
        id = person.save()
        :return: Primary key
        """
        log_support.orm_inst_log('inst_save', self.__class__.__name__)
        key = self._get_key()
        kv = self._get_kv(ignored_none, None, *fields)
        _id = self.save(**kv)
        if key not in kv:
            self.__dict__.update({key: _id})
        return _id

    def update(self, *fields, ignored_none=True) -> int:
        """
        person = Person(id=1, name='李四', age=66)
        rowcount = person.update()
        :return: Effect rowcount
        """
        log_support.orm_inst_log('update', self.__class__.__name__)
        key, table = self._get_key_and_table()
        kv = self._get_kv(ignored_none, key, *fields)
        _id = kv[key]
        assert _id is not None, 'Primary key must not be None.'
        update_kv = {k: v for k, v in kv.items() if k != key}
        if update_kv:
            return self.update_by_id(_id, **update_kv)
        else:
            log_support.logger.warning("Exec func 'sqlbatis.sqlormx.Model.%s' not set fields, Class: '%s:'\n\t   %s" % ('update', self.__class__.__name__, self))
            return 0

    def load(self, *fields) -> 'Model':
        """
        Return new object from database and update itself.
        :param fields: Default select all fields if not set. like: ('id', 'name', 'age')
        person = Person(id=1)
        person2 = person.load()
        """
        log_support.logger.debug("Exec func 'sqlbatis.sqlormx.Model.%s', Class: '%s', fields: %s" % ('load', self.__class__.__name__, fields))
        key = self._get_key()
        kv = self.__dict__
        _id = kv.get(key)
        assert _id is not None, 'Primary key must not be None.'
        if not fields:
            fields, _ = zip(*kv.items())
        result = self.query_by_id(_id, *fields)
        if result:
            self.__dict__.update(result)
            return self
        else:
            raise NotFoundError("Load not found from db, Class: '%s', %s=%d." % (self.__class__.__name__, key, _id))

    def logical_delete(self) -> int:
        """
        Logic delete only update the del flag
        person = Person(id=1)
        rowcount = person.logical_delete()
        """
        log_support.orm_inst_log('logical_delete', self.__class__.__name__)
        key = self._get_key()
        kv = self.__dict__
        _id = kv.get(key)
        assert _id is not None, 'Primary key must not be None.'
        update_by = kv.get(self._get_update_by_field())
        return self.logical_delete_by_id(_id, update_by)

    def logical_undelete(self) -> int:
        """
        Logic un delete only update the del flag
        person = Person(id=1)
        rowcount = person.logical_undelete()
        """
        log_support.orm_inst_log('logical_undelete', self.__class__.__name__)
        key = self._get_key()
        kv = self.__dict__
        _id = kv.get(key)
        assert _id is not None, 'Primary key must not be None.'
        update_by = kv.get(self._get_update_by_field())
        return self.logical_undelete_by_id(_id, update_by)

    def remove(self) -> int:
        """
        Physical delete
        person = Person(id=1)
        rowcount = person.remove()
        """
        log_support.orm_inst_log('remove', self.__class__.__name__)
        key = self._get_key()
        _id = self.__dict__.get(key)
        assert _id is not None, 'Primary key must not be None.'
        return self.delete_by_id(_id)

    # ----------------------------------------------------------Class method------------------------------------------------------------------
    @classmethod
    def insert(cls, **kwargs) -> int:
        """
        rowcount = Person.insert(name='张三', age=20)
        return: Effect rowcount
        """
        log_support.orm_insert_log('insert', cls.__name__, **kwargs)
        key, table = cls._get_key_and_table()
        key_strategy = cls._get_key_strategy()
        if key_strategy == KeyStrategy.SNOWFLAKE and key not in kwargs:
            kwargs[key] = get_snowflake_id()
        return db.insert(table, **kwargs)

    @classmethod
    def save(cls, **kwargs) -> Any:
        """
        id = Person.save(name='张三', age=20)
        :return: Primary key
        """
        log_support.orm_insert_log('save', cls.__name__, **kwargs)
        key, table = cls._get_key_and_table()
        if key in kwargs:
            db.insert(table, **kwargs)
            return kwargs[key]

        key_strategy = cls._get_key_strategy()
        if key_strategy == KeyStrategy.SNOWFLAKE:
            kwargs[key] = get_snowflake_id()
            db.insert(table, **kwargs)
            return kwargs[key]
        else:
            select_key = cls._get_select_key()
            if not select_key:
                keq_seq = cls._get_key_seq()
                try:
                    select_key = db.Dialect.get_select_key(keq_seq=keq_seq, table=table, key=key)
                except NotImplementedError:
                    raise DBError("Expect 'select_key'. you can set it in model class with '__select_key__'. "
                                  "You can also set primary key sequence with '__key_seq__' for PostgreSQL.'")
            return db.save_select_key(select_key, table, **kwargs)

    @classmethod
    def create(cls, **kwargs) -> int:
        """
        person = Person.create(name='张三', age=20)
        :return: Instance object
        """
        log_support.orm_insert_log('create', cls.__name__, **kwargs)
        key = cls._get_key()
        kwargs[key] = cls.save(**kwargs)
        return cls.to_obj(**kwargs)

    @classmethod
    def update_by_id(cls, pk: Union[int, str], **kwargs) -> int:
        """
        rowcount = Person.update_by_id(id=1, name='王五')
        return: Effect rowcount
        """
        log_support.logger.debug("Exec func 'sqlbatis.sqlormx.Model.%s' \n\t Class: '%s', id: %d, kwargs: %s" % ('update_by_id', cls.__name__, pk, kwargs))
        assert kwargs, 'Must set update kv'
        key, table_name = cls._get_key_and_table()
        where_kwargs = {key: pk}
        kwargs = cls._update_time(**kwargs)
        return db.table(table_name).where(**where_kwargs).update(**kwargs)

    @classmethod
    def logical_delete_by_id(cls, pk: Union[int, str], update_by: Union[int, str] = None) -> int:
        """
        Logic delete only update the del flag
        rowcount = Person.delete_by_id(id=1, update_by=100)
        return: Effect rowcount
        """
        log_support.orm_delete_by_id_log('logical_delete_by_id', cls.__name__, pk, update_by)
        return cls._logical_delete_by_id_op(pk, update_by, DelFlag.DELETED)

    @classmethod
    def logical_undelete_by_id(cls, pk: Union[int, str], update_by: Union[int, str] = None) -> int:
        """
        Logic delete only update the del flag
        rowcount = Person.logical_undelete_by_id(id=1, update_by=100)
        return: Effect rowcount
        """
        log_support.orm_delete_by_id_log('logical_undelete_by_id', cls.__name__, pk, update_by)
        return cls._logical_delete_by_id_op(pk, update_by, DelFlag.UN_DELETE)

    @classmethod
    def logical_delete_by_ids(cls, ids: Union[Sequence[int], Sequence[str]], update_by: Union[int, str] = None,
                              batch_size=128) -> int:
        """
        Logic delete only update the del flag
        rowcount = Person.logical_delete_by_ids(id=[1,2], update_by=100)
        return: Effect rowcount
        """
        log_support.orm_logical_delete_by_ids_log('logical_delete_by_ids', cls.__name__, ids, update_by, batch_size)
        return cls._logical_delete_by_ids_op(ids, update_by=update_by, batch_size=batch_size, del_status=DelFlag.DELETED)

    @classmethod
    def logical_undelete_by_ids(cls, ids: Union[Sequence[int], Sequence[str]], update_by: Union[int, str] = None,
                                batch_size=128) -> int:
        """
        Logic delete only update the del flag
        rowcount = Person.logical_undelete_by_ids(id=[1,2], update_by=100)
        return: Effect rowcount
        """
        log_support.orm_logical_delete_by_ids_log('logical_undelete_by_ids', cls.__name__, ids, update_by, batch_size)
        return cls._logical_delete_by_ids_op(ids, update_by=update_by, batch_size=batch_size, del_status=DelFlag.UN_DELETE)

    @classmethod
    def delete(cls, **kwargs) -> int:
        """
        Physical delete
        rowcount = Person.delete(name='张三', age=55)
        return: Effect rowcount
        """
        log_support.orm_count_log(sys._getframe().f_code.co_name, cls.__name__, **kwargs)
        table = cls.get_table()
        return db.table(table).where(**kwargs).delete()

    @classmethod
    def delete_by_id(cls, pk: Union[int, str]) -> int:
        """
        Physical delete
        rowcount = Person.delete_by_id(id=1)
        return: Effect rowcount
        """
        log_support.logger.debug("Exec func 'sqlbatis.sqlormx.Model.%s' \n\t Class: '%s', id: %d" % ('delete_by_id', cls.__name__, pk))
        key, table = cls._get_key_and_table()
        where_kwargs = {key: pk}
        return db.table(table).where(**where_kwargs).delete()

    @classmethod
    def delete_by_ids(cls, ids: Union[Sequence[int], Sequence[str]], batch_size=128) -> int:
        """
        Batch physical delete, they will be executed in batches if there are too many
        rowcount = Person.delete_by_ids(id=[1,2])
        return: Effect rowcount
        """
        log_support.logger.debug("Exec func 'sqlbatis.sqlormx.Model.%s' \n\t Class: '%s', ids: %s, batch_size: %s" % ('delete_by_ids', cls.__name__, ids, batch_size))
        ids_size = len(ids)
        assert ids_size > 0, 'ids must not be empty.'
        if ids_size == 1:
            return cls.delete_by_id(ids[0])
        elif ids_size <= batch_size:
            return cls.do_delete_by_ids(ids)
        else:
            slices = orm_support.split_ids(ids, batch_size)
            with db.transaction():
                results = list(map(cls.do_delete_by_ids, slices))
            return sum(results)

    @classmethod
    def do_delete_by_ids(cls, ids: Union[Sequence[int], Sequence[str]]) -> int:
        """
        Batch physical delete, please use delete_by_ids if there are too many
        rowcount = Person.do_delete_by_ids(id=[1,2])
        return: Effect rowcount
        """
        key, table = cls._get_key_and_table()
        where_kwargs = {'{}__in'.format(key): ids}
        return db.table(table).where(**where_kwargs).delete()

    @classmethod
    def batch_insert(cls, *args) -> int:
        """
        Batch insert
        rowcount = Person.batch_insert([{'name': '张三', 'age': 55},{'name': '李四', 'age': 66}])
        :param args: All number must have same key.
        :return: Effect rowcount
        """
        log_support.logger.debug("Exec func 'sqlbatis.sqlormx.Model.%s' \n\t Class: '%s', args: %s" % ('batch_insert', cls.__name__, args))
        assert len(args) > 0, 'args must not be empty.'
        key, table = cls._get_key_and_table()
        key_strategy = cls._get_key_strategy()
        if key_strategy == KeyStrategy.SNOWFLAKE:
            for arg in args:
                if key not in arg:
                    arg[key] = get_snowflake_id()

        return db.batch_insert(table, *args)

    # ------------------------------------------------Class query method------------------------------------------------
    @classmethod
    def count(cls, **kwargs) -> int:
        """
        count = Person.count(name='张三', age=55)
        """
        log_support.orm_count_log('count', cls.__name__, **kwargs)
        table = cls.get_table()
        return db.table(table).where(**kwargs).count()

    @classmethod
    def exists(cls, **kwargs) -> bool:
        log_support.orm_count_log('exists', cls.__name__, **kwargs)
        table = cls.get_table()
        return db.table(table).where(**kwargs).exists()

    @classmethod
    def exists_by_id(cls, pk: Union[int, str]) -> bool:
        key = cls._get_key()
        kwargs = {key: pk}
        return cls.exists(**kwargs)

    @classmethod
    def find(cls, *fields, **kwargs) -> List['Model']:
        """
        Return list(object) or empty list if no result.
        persons = Person.find('id', 'name', 'age', name='张三', age=55)
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_log('find', cls.__name__, *fields, **kwargs)
        return [cls.to_obj(**d) for d in cls.query(*fields, **kwargs)]

    @classmethod
    def find_one(cls, *fields, **kwargs) ->'Model':
        """
        Return unique result(object) or None if no result.
        person = Person.find_one('id', 'name', 'age', name='张三', age=55)
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_log('find_one', cls.__name__, *fields, **kwargs)
        result = cls.query_one(*fields, **kwargs)
        return cls.to_obj(**result) if result else None

    @classmethod
    def find_first(cls, *fields, **kwargs) ->'Model':
        """
        Return first result(object) or None if no result.
        person = Person.find_first('id', 'name', 'age', name='张三')
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_log('find_first', cls.__name__, *fields, **kwargs)
        result = cls.query_first(*fields, **kwargs)
        return cls.to_obj(**result) if result else None

    @classmethod
    def find_by_id(cls, pk: Union[int, str], *fields) ->'Model':
        """
        Return one class object or None if no result.
        person = Person.find_by_id(1, 'id', 'name', 'age')
        :param pk: primary key
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_by_id_log('find_by_id', cls.__name__, pk, *fields)
        result = cls.query_by_id(pk, *fields)
        return cls.to_obj(**result) if result else None

    @classmethod
    def find_by_ids(cls, ids: Union[Sequence[int], Sequence[str]], *fields) -> List['Model']:
        """
        Return list(class object) or empty list if no result.
        persons = Person.find_by_ids([1,2], 'id', 'name', 'age')
        :param ids: List of key
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_by_ids_log('find_by_ids', cls.__name__, ids, *fields)
        return [cls.to_obj(**d) for d in cls.query_by_ids(ids, *fields)]

    @classmethod
    def query(cls, *fields, **kwargs) -> List[dict]:
        """
        Return list(dict) or empty list if no result.
        persons = Person.query('id', 'name', 'age', name='张三', age=55)
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_log('query', cls.__name__, *fields, **kwargs)
        table = cls.get_table()
        return db.table(table).columns(*fields).where(**kwargs).query()

    @classmethod
    def query_one(cls, *fields, **kwargs) -> dict:
        """
        Return unique result(dict) or None if no result.
        persons = Person.query_one('id', 'name', 'age', name='张三', age=55)
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_log('query_one', cls.__name__, *fields, **kwargs)
        table = cls.get_table()
        return db.table(table).columns(*fields).where(**kwargs).query_one()

    @classmethod
    def query_first(cls, *fields, **kwargs) -> dict:
        """
        Return first result(dict) or None if no result.
        person = Person.query_first('id', 'name', 'age', name='张三')
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_log('query_first', cls.__name__, *fields, **kwargs)
        table = cls.get_table()
        return db.table(table).columns(*fields).where(**kwargs).query_first()

    @classmethod
    def query_by_id(cls, pk: Union[int, str], *fields) -> dict:
        """
        Return one row(dict) or None if no result.
        person = Person.query_by_id(1, 'id', 'name', 'age')
        :param pk: key
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_by_id_log('query_by_id', cls.__name__, pk, *fields)
        key, table = cls._get_key_and_table()
        kwargs = {key: pk}
        return db.table(table).columns(*fields).where(**kwargs).query_one()

    @classmethod
    def query_by_ids(cls, ids: Union[Sequence[int], Sequence[str]], *fields) -> List[dict]:
        """
        Return list(dict) or empty list if no result.
        persons = Person.query_by_ids([1,2], 'id', 'name', 'age')
        :param ids: List of key
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_by_ids_log('query_by_ids', cls.__name__, ids, *fields)
        assert len(ids) > 0, 'ids must not be empty.'

        key, table = cls._get_key_and_table()
        kwargs = {'{}__in'.format(key): ids}
        return db.table(table).columns(*fields).where(**kwargs).query()

    @classmethod
    def select(cls, *fields, **kwargs) -> List[Tuple]:
        """
        Return list(dict) or empty list if no result.
        rows = Person.select('id', 'name', 'age', name='张三', age=55)
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_log('select', cls.__name__, *fields, **kwargs)
        table = cls.get_table()
        return db.table(table).columns(*fields).where(**kwargs).select()

    @classmethod
    def select_one(cls, *fields, **kwargs) -> Tuple:
        """
        Return unique result(tuple) or None if no result.
        row = Person.select_one('id', 'name', 'age', name='张三', age=55)
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_log('select_one', cls.__name__, *fields, **kwargs)
        table = cls.get_table()
        return db.table(table).columns(*fields).where(**kwargs).select_one()

    @classmethod
    def select_first(cls, *fields, **kwargs) -> Tuple:
        """
        Return first result(tuple) or None if no result.
        row = Person.select_first('id', 'name', 'age', name='张三')
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_log('select_first', cls.__name__, *fields, **kwargs)
        table = cls.get_table()
        return db.table(table).columns(*fields).where(**kwargs).select_first()

    @classmethod
    def select_by_id(cls, pk: Union[int, str], *fields) -> Tuple:
        """
        Return one row(dict) or None if no result.
        row = Person.select_by_id(1, 'id', 'name', 'age')
        :param pk: primary key
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_by_id_log('select_by_id', cls.__name__, pk, *fields)
        key, table = cls._get_key_and_table()
        kwargs = {key: pk}
        return db.table(table).columns(*fields).where(**kwargs).select_one()

    @classmethod
    def select_by_ids(cls, ids: Union[Sequence[int], Sequence[str]], *fields) -> List[Tuple]:
        """
        Return list(dict) or empty list if no result.
        rows = Person.select_by_ids([1,2], 'id', 'name', 'age')
        :param ids: List of key
        :param fields: Default select all fields if not set
        """
        log_support.orm_find_by_ids_log('select_by_ids', cls.__name__, ids, *fields)
        assert len(ids) > 0, 'ids must not be empty.'

        key, table = cls._get_key_and_table()
        kwargs = {'{}__in'.format(key): ids}
        return db.table(table).columns(*fields).where(**kwargs).select()

    @classmethod
    def ravel_list(cls, field: str, **kwargs) -> List:
        """
        Return list or empty list if no result.
        results = Person.ravel_list('name', age=20)
        :param field:
        """
        log_support.orm_find_log('ravel_list', cls.__name__, field, **kwargs)
        table = cls.get_table()
        return db.table(table).columns(field).where(**kwargs).ravel_list()

    @classmethod
    def find_page(cls, page_num=1, page_size=10, *fields, return_total: bool = False, **kwargs) -> List['Model']:
        """
        Return list(object) or empty list if no result.
        persons = Person.find_page(1, 10, 'name', 'age', name='张三', age=55)
        :param page_num: page number
        :param page_size: page size
        :param fields: Default select all fields if not set
        :param return_total: 是否返回total, if true, return (total, list(object), else return list(object)
        """
        log_support.orm_page_log('find_page', page_num, page_size, cls.__name__, *fields, **kwargs)
        if return_total:
            total, result = cls.query_page(page_num, page_size, *fields, return_total=True, **kwargs)
            return total, [cls.to_obj(**d) for d in result]
        result = cls.query_page(page_num, page_size, *fields, **kwargs)
        return [cls.to_obj(**d) for d in result]

    @classmethod
    def query_page(cls, page_num=1, page_size=10, *fields, return_total: bool = False, **kwargs) -> List[dict]:
        """
        Return list(dict) or empty list if no result.
        persons = Person.query_page(1, 10, 'id', 'name', 'age', name='张三', age=55)
        :param page_num: page number
        :param page_size: page size
        :param return_total: 是否返回total, if true, return (total, list(dict), else return list(dict)
        """
        log_support.orm_page_log('query_page', page_num, page_size, cls.__name__, *fields, **kwargs)
        table = cls.get_table()
        return db.table(table).columns(*fields).where(**kwargs).page(page_num, page_size, return_total).query()

    @classmethod
    def select_page(cls, page_num=1, page_size=10, *fields, return_total: bool = False, **kwargs) -> List[Tuple]:
        """
        Return list(tuple) or empty list if no result.
        rows = Person.select_page('id', 'name', 'age', name='张三', age=55)
        :param page_num: page number
        :param page_size: page size
        :param fields: Default select all fields if not set
        :param return_total: 是否返回total, if true, return (total, list(tuple), else return list(tuple)
        """
        log_support.orm_page_log('select_page', page_num, page_size, cls.__name__, *fields, **kwargs)
        table = cls.get_table()
        return db.table(table).columns(*fields).where(**kwargs).page(page_num, page_size, return_total).select()

    @classmethod
    def fields(cls, *fields) -> orm_support.FieldExec:
        return orm_support.FieldExec(cls, *fields)

    @classmethod
    def where(cls, **kwargs) -> orm_support.WhereExec:
        return orm_support.WhereExec(cls, **kwargs)

    @classmethod
    def page(cls, page_num=1, page_size=10, return_total: bool = False) -> orm_support.PageExec:
        return orm_support.PageExec(cls, page_num, page_size, return_total)

    @classmethod
    def to_obj(cls, **kwargs):
        model = cls.__new__(cls)
        model.__dict__.update(**kwargs)
        return model

    def _get_kv(self, ignored_none: bool, key: None, *fields):
        if fields:
            if key:
                fields = (key, *fields)
            if ignored_none:
                return {k: v for k, v in self.__dict__.items() if v is not None and k in fields}
            return {k: v for k, v in self.__dict__.items() if k in fields}

        if ignored_none:
            return {k: v for k, v in self.__dict__.items() if v is not None}
        return {k: v for k, v in self.__dict__.items()}

    # ------------------------------------------------Private class method----------------------------------------------
    @classmethod
    def _logical_delete_by_id_op(cls, pk: Union[int, str], update_by: Union[int, str] = None, del_status=DelFlag.DELETED):
        key, table = cls._get_key_and_table()
        del_flag_field = cls._get_del_flag_field()
        update_by_field = cls._get_update_by_field()

        where = '%s = ?' % key
        if update_by is not None and update_by_field is not None:
            sql, update_time_arg = cls._update_sql(where, del_flag_field, update_by_field)
            if update_time_arg:
                return db.do_execute(sql, del_status.value, update_by, update_time_arg, pk)
            return db.do_execute(sql, del_status.value, update_by, pk)
        else:
            sql, update_time_arg = cls._update_sql(where, del_flag_field)
            if update_time_arg:
                return db.do_execute(sql, del_status.value, update_time_arg, pk)
            return db.do_execute(sql, del_status.value, pk)

    @classmethod
    def _logical_delete_by_ids_op(cls, ids: Union[Sequence[int], Sequence[str]], update_by: Union[int, str] = None,
                                  batch_size=128, del_status=DelFlag.DELETED):
        ids_size = len(ids)
        assert ids_size > 0, 'ids must not be empty.'

        if ids_size == 1:
            return cls._logical_delete_by_id_op(ids[0], update_by, del_status)
        elif ids_size <= batch_size:
            return cls._do_logical_delete_by_ids(ids, update_by, del_status)
        else:
            slices = orm_support.split_ids(ids, batch_size)
            with db.transaction():
                results = [cls._do_logical_delete_by_ids(ids, update_by, del_status) for ids in slices]
            return sum(results)

    @classmethod
    def _do_logical_delete_by_ids(cls, ids: Union[Sequence[int], Sequence[str]], update_by: Union[int, str] = None, del_status=DelFlag.DELETED):
        key = cls._get_key()
        del_flag_field = cls._get_del_flag_field()
        update_by_field = cls._get_update_by_field()

        where = '%s in (%s)' % (key, ','.join(['?' for _ in range(len(ids))]))
        if update_by is not None and update_by_field is not None:
            sql, update_time_arg = cls._update_sql(where, del_flag_field, update_by_field)
            if update_time_arg:
                return db.do_execute(sql, del_status.value, update_by, update_time_arg, *ids)
            return db.do_execute(sql, del_status.value, update_by, *ids)
        else:
            sql, update_time_arg = cls._update_sql(where, del_flag_field)
            if update_time_arg:
                return db.do_execute(sql, del_status.value, update_time_arg, *ids)
            return db.do_execute(sql, del_status.value, *ids)

    @classmethod
    def _get_key(cls):
        if hasattr(cls, KEY):
            return cls.__key__
        log_support.logger.warning(f"'{cls.__name__}' class not set attribute '{KEY}'")
        return DEFAULT_KEY_FIELD

    @classmethod
    def _get_select_key(cls):
        return cls.__select_key__ if hasattr(cls, SELECT_KEY) else None

    @classmethod
    def _get_key_seq(cls):
        return cls.__key_seq__ if hasattr(cls, KEY_SEQ) else None

    @classmethod
    @lru_cache(maxsize=lru_cache_size)
    def get_table(cls):
        if hasattr(cls, TABLE):
            return cls.__table__
        log_support.logger.warning(f"'{cls.__name__}' class not set attribute '{TABLE}'")
        return orm_support.get_table_name(cls.__name__)

    @classmethod
    def _get_key_and_table(cls):
        return cls._get_key(), cls.get_table()

    @classmethod
    def _get_key_strategy(cls):
        if hasattr(cls, KEY_STRATEGY):
            return cls.__key_strategy__
        return None

    @classmethod
    def _get_update_by_field(cls):
        if hasattr(cls, UPDATE_BY):
            return cls.__update_by__
        return None

    @classmethod
    def _get_update_time_field(cls):
        if hasattr(cls, UPDATE_TIME):
            return cls.__update_time__
        return None

    @classmethod
    def _get_del_flag_field(cls):
        assert hasattr(cls, DEL_FLAG), "%s not set attribute '%s'" % (cls.__name__, DEL_FLAG)
        return cls.__del_flag__

    @classmethod
    def _update_time(cls, **kwargs):
        update_time_field = cls._get_update_time_field()
        if update_time_field is not None and update_time_field not in kwargs:
            kwargs[update_time_field] = datetime.now()
        return kwargs

    @classmethod
    def _update_sql(cls, where, *update_fields):
        update_time_arg = None
        table = cls.get_table()
        table = db.Dialect.get_dialect_str(table)
        update_time_field = cls._get_update_time_field()
        if update_time_field is not None and update_time_field not in update_fields:
            update_fields = [*update_fields, update_time_field]
            update_time_arg = datetime.now()

        update_fields = ', '.join(['{} = ?'.format(db.Dialect.get_dialect_str(col)) for col in update_fields])
        return 'UPDATE {} SET {} WHERE {}'.format(table, update_fields, where), update_time_arg
