import time

from homework3.task02.task_02 import pool_handler, slow_calculate


def test_pool_handler():
    """Testing than pool_handler faster then call function with one process"""
    data = range(0, 5)
    t0 = time.time()
    pool_handler(data)
    t1 = time.time()
    for value in range(0, 5):
        slow_calculate(value)
    t2 = time.time()
    assert t1 - t0 < t2 - t1
