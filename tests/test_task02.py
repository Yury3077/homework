import pytest

from Tasks02_05.task02 import check_fibonacci


def test_positive_case():
    """Testing that sequence is a Fibonacci sequence"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5])


def test_negative_case():
    """Testing that sequence i'snt a Fibonacci sequence"""
    assert not check_fibonacci([0, 1, 1, 11, 3, 5])


def test_with_one_number():
    """Testing that sequence i'snt a Fibonacci sequence because has only one number"""
    assert not check_fibonacci([17])
