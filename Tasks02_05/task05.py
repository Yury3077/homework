"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List
from math import inf


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    find maximal value in sub-array with length <= k
    :param nums: list of integer numbers
    :param k: integer number for separating list into sub-array
    :return: maximal sum of sub-arrays
    """
    max_value = -inf
    for j in range(len(nums)):
        for i in range(k):
            sum_sub_list = sum(nums[j:j + i + 1])
            if sum_sub_list >= max_value:
                max_value = sum_sub_list
    return max_value
