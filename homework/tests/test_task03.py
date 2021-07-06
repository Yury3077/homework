import os

from homework.tasks02_05.task03 import find_maximum_and_minimum


def test_find_maximum_and_minimum_in_file_with_nums():
    """Testing that function find min and max in file"""
    path_dir = os.getcwd()
    assert find_maximum_and_minimum(
        os.path.join(path_dir, "homework/tests/some_file.txt")
    ) == [(1, 613)]
