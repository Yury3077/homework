import pytest
from homework2.hw3 import combinations


def test_positive_case():
    """Testing that take function return combinations of lists of K items  """
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]
