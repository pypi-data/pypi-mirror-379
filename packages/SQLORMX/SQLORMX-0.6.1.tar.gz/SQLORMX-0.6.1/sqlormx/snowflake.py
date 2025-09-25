__doc__ = """
默认worker_bits=3, sequence_bits=6。
不区分数据中心，机器id最多2^3=8 台，每秒最大并发为2^6*1000=64000，使用超过40年id的长度也不超过15位，javascript可以直接使用，不需转化为string
"""

import time
from threading import RLock

_SNOWFLAKE = None
# _SEQUENCE_MASK = 4095


class SnowflakeError(Exception):
    pass


def init_snowflake(epoch=1688140800000, machine_id=0, worker_bits=3, sequence_bits=6):
    global _SNOWFLAKE
    if _SNOWFLAKE is not None:
        SnowflakeError("Snowflake was already initialized.")
    _SNOWFLAKE = Snowflake(machine_id, epoch, worker_bits, sequence_bits)


def get_snowflake_id():
    global _SNOWFLAKE
    try:
        return _SNOWFLAKE.generate_id()
    except AttributeError:
        raise RuntimeError("Please init Snowflake first with: snowflake.init_snowflake(...)")


def _get_timestamp():
    return int(time.time() * 1000)


def _wait_next_millis(last_timestamp):
    timestamp = _get_timestamp()
    while timestamp <= last_timestamp:
        timestamp = _get_timestamp()
    return timestamp


class Snowflake:
    def __init__(self, machine_id: int, epoch: int, worker_bits: int, sequence_bits: int):
        self.machine_id = machine_id
        self.epoch = epoch
        self.sequence = 0
        self.last_timestamp = -1
        self.worker_shift = sequence_bits
        self.sequence_mask = -1 ^ (-1 << sequence_bits)
        self.timestamp_left_shift = worker_bits + sequence_bits
        self.lock = RLock()

        maxWorkerId = -1 ^ (-1 << worker_bits);
        assert 0 <= machine_id < maxWorkerId, 'machine_id must ge 0 and lt %d, but it is %d' % (maxWorkerId, machine_id)
        # assert 10 <= self.timestamp_left_shift <= 22, 'worker_bits add sequence_bits must between 10 and 20, but it is %d' % self.timestamp_left_shift

    def generate_id(self):
        with self.lock:
            timestamp = _get_timestamp()
            if timestamp < self.last_timestamp:
                raise Exception("Clock moved backwards")
            if timestamp == self.last_timestamp:
                self.sequence = (self.sequence + 1) & self.sequence_mask
                if self.sequence == 0:
                    timestamp = _wait_next_millis(self.last_timestamp)
            else:
                self.sequence = 0
            self.last_timestamp = timestamp
            return ((timestamp - self.epoch) << self.timestamp_left_shift) | (self.machine_id << self.worker_shift) | self.sequence
            # return ((timestamp - 1288834974657) << 22) | (self.machine_id << 12) | self.sequence
