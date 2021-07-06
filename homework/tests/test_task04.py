from homework.tasks02_05.task04 import check_sum_of_four


def test_check_sum_of_four_nums_from_list_give_zero():
    """Testing that function calculates combination in lists numbers that give zero"""
    l1 = [1, -2, 4, -5, 9]
    l2 = [1, -4, -6, 11, 10]
    l3 = [-4, 7, -2, 11, 1]
    l4 = [-10, 8, -7, 6, 20]
    assert check_sum_of_four(l1, l2, l3, l4) == 15
