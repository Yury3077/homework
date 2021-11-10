from homework3.task04.task04 import is_armstrong


def test_is_armstrong_num_153():
    """Testing that number 153 is Armstrong num"""
    assert is_armstrong(153)


def test_is_armstrong_num_10():
    """Testing that number 153 is not Armstrong num"""
    assert not is_armstrong(10)
