import pytest
import string
from homework2.hw5 import custom_range


def test_positive_case():
    """Testing that return a part with 1 argument"""
    assert custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']


def test_positive_case_2():
    """Testing that return a part with 2 argument"""
    assert custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


def test_positive_case_3():
    """Testing that return a part with 3 argument"""
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
