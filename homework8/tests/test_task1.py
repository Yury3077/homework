import os

from homework8.task1 import KeyValueStorage


def test_get_item_from_instance():
    """Checking that get item from instance"""
    path = os.path.join(os.getcwd(), "homework8/task1.txt")
    storage = KeyValueStorage(path)
    assert storage["name"] == "kek"


def test_get_item_as_a_method():
    """Checking that get value use a method as a key"""
    path = os.path.join(os.getcwd(), "homework8/task1.txt")
    storage = KeyValueStorage(path)
    assert storage.song == "shadilay"


def test_get_item_as_a_method_integer():
    """Checking that custom dict save integers"""
    path = os.path.join(os.getcwd(), "homework8/task1.txt")
    storage = KeyValueStorage(path)
    assert type(storage.power) == int
