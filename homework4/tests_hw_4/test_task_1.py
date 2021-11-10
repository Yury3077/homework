import os

import pytest

from homework4.task_1_read_file import read_magic_number


def test_file_contain_num_in_the_first_line_return_true():
    """Testing that function return TRUE if read number 2 in the 1st line"""
    try:
        text_file = open("text_with.txt", "w")
        text_file.write("2")
        text_file.close()
        path_dir = os.getcwd()
        assert read_magic_number(os.path.join(path_dir, "text_with.txt"))
    finally:
        os.remove(os.path.join(path_dir, "text_with.txt"))


def test_file_contain_num_in_the_first_line_return_false():
    """
    Testing that function return FALSE if read number 10 in the 1st line
    """
    try:
        text_file = open("text_with.txt", "w")
        text_file.write("10")
        text_file.close()
        path_dir = os.getcwd()
        assert not read_magic_number(os.path.join(path_dir, "text_with.txt"))
    finally:
        os.remove(os.path.join(path_dir, "text_with.txt"))


def test_file_contain_num_in_the_first_line_return_value_error():
    """
    Testing that function return error if read not number in the 1st line
    """
    try:
        text_file = open("text_with.txt", "w")
        text_file.write("rrrr")
        text_file.close()
        path_dir = os.getcwd()
        with pytest.raises(ValueError):
            read_magic_number(os.path.join(path_dir, "text_with.txt"))
    finally:
        os.remove(os.path.join(path_dir, "text_with.txt"))
