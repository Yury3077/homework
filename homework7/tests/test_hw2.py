from homework7.hw2 import backspace_compare


def test_two_str_with_same_output_str():
    """Test that function return True if we "#" symbol like backspace"""
    str_1 = "we#c"
    str_2 = "wetr###c"
    assert backspace_compare(str_1, str_2)


def test_two_str_with_not_the_same_output_str():
    """Testing that function return False if use different amount of "#" to the same string"""
    str_3 = "can#"
    str_4 = "can##"
    assert not backspace_compare(str_3, str_4)
