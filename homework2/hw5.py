"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import List


def custom_range(iterable_obj: str, *args) -> List[str]:
    """
    accept any iterable of unique values and then
    it behaves as range function
    :param iterable_obj: input string data
    :param args: keyword arguments can be 1-3 values
    :return: a range of iterable object
    """
    step = 1
    if len(args) == 1:
        start = iterable_obj[0]
        end = args[0]
    elif len(args) == 2:
        start = args[0]
        end = args[1]
    else:
        start = args[0]
        end = args[1]
        step = args[2]
    list_result = []
    start_num = iterable_obj.find(start)
    end_num = iterable_obj.find(end)
    for i in range(start_num, end_num, step):
        list_result.append(iterable_obj[i])
    return list_result
