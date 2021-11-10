from homework4.task_3_get_print_output import my_precious_logger


def test_some_error_in_str_return_error_in_terminal(capfd):
    """Checking that func return an error into terminal"""
    my_precious_logger("error: file not found")
    out, err = capfd.readouterr()
    assert err == "error: file not found\n"


def test_some_str_return_a_string_in_terminal(capfd):
    """Checking that func return a massage into terminal"""
    my_precious_logger("error: file not found")
    my_precious_logger("OK")
    out, err = capfd.readouterr()
    assert out == "OK\n"
