import os

from homework9.hw3 import universal_file_counter


def test_count_lines_without_tokenizer():
    path = os.path.join(os.getcwd(), "homework9")
    assert universal_file_counter(path, "txt") == 15


def test_count_lines_with_tokenizer():
    path = os.path.join(os.getcwd(), "homework9")
    assert universal_file_counter(path, "txt", str.split) == 17
