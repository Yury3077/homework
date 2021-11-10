"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    """
    Accept another function as an argument. Then it
    should return such a function, so the every call to initial one
    should be cached
    :param func: another func with parameters
    :return: decorated func
    """
    def wrapper(*args, **kwargs):
        dict_key = args
        if dict_key not in wrapper.cache:
            wrapper.cache[dict_key] = func(*args, **kwargs)
        return wrapper.cache[dict_key]
    wrapper.cache = dict()
    return wrapper
