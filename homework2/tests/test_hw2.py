import pytest
from homework2.hw2 import major_and_minor_elem


def test_positive_case():
    """Testing that find max and min in list"""
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)


def test_positive_case_2():
    """Testing that find max and min in list"""
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_positive_case_3():
    """Testing that find max and min in short list"""
    assert major_and_minor_elem([2]) == (2, 2)
