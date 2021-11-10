from homework5.save_original_info import custom_sum


def test_sum_two_lists():
    """Testing sum of two lists turn to one"""
    assert custom_sum([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]


def test_sum_nums():
    """Testing func than sum numbers"""
    assert custom_sum(1, 2, 3, 4) == 10


def test_save_original_name_and_doc():
    """Testing that func return original doc and name"""
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
    assert custom_sum.__name__ == "custom_sum"


def test_return_value_without_print():
    """Testing than save original func and return value without print"""
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10
