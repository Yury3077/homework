import pytest

from homework3.task01.task_01 import decorator_with_parameter


def test_decorator_with_parametr():
    """Testing than inner decorated function call only 3 times from cache"""

    @decorator_with_parameter(3)
    def func(a, b):
        return (a + b) * 2

    some = 100, 200
    val_1 = func(*some)
    val_2 = func(*some)
    val_3 = func(*some)
    val_4 = func(*some)
    assert val_1 is val_2
    assert val_1 is not val_4
