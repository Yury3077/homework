import os

from homework.Tasks02_05.task03 import find_maximum_and_minimum


def test_find_maximum_and_minimum_in_file_with_nums():
    """Testing that function find min and max in file"""
    path_absolute = os.path.abspath("some_file.txt")
    assert find_maximum_and_minimum(path_absolute) == [
        (1, 613),
        (4, 190),
        (-12, 16),
        (0, 0),
    ]
