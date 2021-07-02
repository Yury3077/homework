import pytest
from Tasks02_05.task05 import find_maximal_subarray_sum


def test_find_maximal_subarray_sum_of_3():
    """Testing that function find max value in sub-array"""
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    assert find_maximal_subarray_sum(nums, k) == 16


def test_test_find_maximal_subarray_sum_of_3_with_one_elem():
    """Testing that function separate sub-arrays in k<=3 and find max"""
    nums = [1, 3, -1, 5 - 3, 5, 3, -80, 100]
    k = 3
    assert find_maximal_subarray_sum(nums, k) == 100
