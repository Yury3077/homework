"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    checking sequence is it a Fibonacci sequence
    if sequence contain only 1 number -> it's not sequence -> return: False
    :param data: Sequence[int]
    :return: True/False
    """
    fib_sequence = [0, 1]
    for i in range(len(data) - 2):
        fib_sequence.append(fib_sequence[i] + fib_sequence[i + 1])
    return fib_sequence == data
