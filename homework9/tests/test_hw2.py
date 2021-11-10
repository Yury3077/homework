import pytest

from homework9.hw2 import ContextManager, ignoring_error


def test_rise_index_error_in_class_context_manager():
    with ContextManager(IndexError):
        raise IndexError
    assert True


def test_put_zero_div_error_in_class_context_manager_but_raise_index_error():
    with pytest.raises(IndexError):
        with ContextManager(ZeroDivisionError):
            raise IndexError


def test_rise_index_error_in_func_context_manager():
    with ignoring_error(ValueError):
        raise ValueError
    assert True


def test_put_name_error_in_func_context_manager_but_raise_type_error():
    with pytest.raises(TypeError):
        with ignoring_error(NameError):
            raise TypeError
