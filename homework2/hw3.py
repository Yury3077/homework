"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any
from itertools import product


def combinations(*args: List[Any]) -> List[List]:
    """
    takes K lists as arguments and returns all possible
    lists of K items where the first element is from the first list,
    the second is from the second and so one
    :param args: lists with input data
    :return: List with possible combinations
    """
    list_result = []
    num = 0
    combinations_iter = product(*args)
    for combination in combinations_iter:  # List[Tuple] -> List[List]
        list_result.append([])
        for elem in combination:
            list_result[num].append(elem)
        num += 1
    return list_result
