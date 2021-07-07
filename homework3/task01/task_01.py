from typing import Callable


def decorator_with_parameter(times):
    """
    Decorator with parameter. Accept another function as an argument. Then it
    should return such a function, so call to initial one
    should be cached several times only
    :param times: amount of times when func take value from cache
    :return: decorated func
    """

    def cache(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            dict_key = args
            if dict_key not in wrapper.cache:
                wrapper.cache[dict_key] = [func(*args, **kwargs), times]
            if wrapper.cache[dict_key][1] >= 1:
                wrapper.cache[dict_key][1] -= 1
                return wrapper.cache[dict_key][0]
            else:
                return func(*args, **kwargs)

        wrapper.cache = dict()
        return wrapper

    return cache
