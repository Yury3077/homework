"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from itertools import product
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    calculates how many combination in list numbers a[i] + b[j] + c[k] + d[l] is zero
    :param a, b, c, d: List[int] length form 0 till 1000
    :return: number of combinations with sum = 0 -> int
    """
    length_list = len(a)
    combinations = product(a, b, c, d)
    counter = 0
    for _ in range(length_list ** 4):
        if sum(next(combinations)) == 0:
            counter += 1
    return counter
