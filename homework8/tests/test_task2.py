import os

import pytest

from homework8.task2 import TableData


def test_not_exist_table_name():
    """Checking that not create an instance if db name or table not exist"""
    path = os.path.join(os.getcwd(), "homework8/example.sqlite")
    with pytest.raises(ValueError):
        TableData(path, "sql injection")


def test_length_of_set():
    """Checking that calculate length of queryset"""
    path = os.path.join(os.getcwd(), "homework8/example.sqlite")
    assert len(TableData(path, "presidents")) == 3


def test_get_item_method():
    """Find a row with in db"""
    path = os.path.join(os.getcwd(), "homework8/example.sqlite")
    assert TableData(path, "presidents")["Yeltsin"] == [("Yeltsin", 999, "Russia")]


def test_if_president_exists_in_table():
    """Checking if we have such name in a table"""
    path = os.path.join(os.getcwd(), "homework8/example.sqlite")
    assert "Yeltsin" in TableData(path, "presidents")
