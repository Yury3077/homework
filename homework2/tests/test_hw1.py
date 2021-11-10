import pytest
from homework2.hw1 import *


def test_positive_case_get_longest_diverse_words():
    """Testing that func read file and find 10 longest words"""
    assert get_longest_diverse_words('test_txt_file.txt') == ['verbirgt.', 'bedenkli-', 'vielmehr', 'Waldgang',
                                                              'Idylle,', 'hinter', 'Titel', 'keine', 'sich', 'Leser']


def test_positive_case_get_rarest_char():
    """Testing that func read file and find the rarest char"""
    assert get_rarest_char('test_txt_file.txt') == "W"


def test_positive_case_count_punctuation_chars():
    """Testing that func read file and count punctuation chars"""
    assert count_punctuation_chars('test_txt_file.txt') == 3


def test_positive_case_count_non_ascii_chars():
    """Testing that func read file and count non ascii chars"""
    assert count_non_ascii_chars('test_txt_file.txt') == 2


def test_positive_case_get_most_common_non_ascii_char():
    """Testing that func read file and find the most common not ascii char"""
    assert get_most_common_non_ascii_char('test_txt_file.txt') == "—"
