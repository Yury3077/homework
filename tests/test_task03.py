import pytest
from Tasks02_05.task03 import find_maximum_and_minimum


def test_equal_values():
    """Testing that function find min and max in each line"""
    assert find_maximum_and_minimum("some_file.txt") == [(1, 613), (4, 190), (-12, 16), (0, 0)]