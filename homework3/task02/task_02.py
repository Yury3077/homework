import hashlib
import multiprocessing
import random
import struct
import time


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def pool_handler(data: int):
    """
    Function that use multiprocessing for faster output of slow_calculate func
    :param data: input value for calculating
    :return: None
    """
    p = multiprocessing.Pool(20)
    p.map(slow_calculate, data)
