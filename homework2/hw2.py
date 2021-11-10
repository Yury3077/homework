"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple
from math import inf


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """
    find most common the least common elem in list
    :param inp: list with input data
    :return: tuple with common, least integers
    """
    dict_counter = {}
    for elem in inp:
        if elem not in dict_counter.keys():
            dict_counter[elem] = 1
        else:
            dict_counter[elem] += 1
    min_key = inf
    max_key = -inf
    common_elem = int
    least_elem = int
    for key in dict_counter.keys():
        if len(inp) // 2 >= 1 and dict_counter[key] > max_key:
            max_key = dict_counter[key]
            common_elem = key
        if dict_counter[key] < min_key:
            min_key = dict_counter[key]
            least_elem = key
    if common_elem is int:
        common_elem = least_elem
    result_tuple = (common_elem, least_elem)
    return result_tuple