from homework7.hw3 import tic_tac_toe_checker


def test_win_x_in_second_row():
    """Testing that x wins in the 2nd row"""
    test_board = [["o", "x", "o"], ["x", "x", "x"], ["o", "o", "x"]]

    assert tic_tac_toe_checker(test_board) == "x wins!"


def test_win_o_in_third_column():
    """Testing that o wins in the 3rd column"""
    test_board_2 = [["o", "x", "o"], ["x", "x", "o"], ["o", "o", "o"]]

    assert tic_tac_toe_checker(test_board_2) == "o wins!"


def test_win_o_in_diagonal():
    """Testing that o wins in diagonal"""
    test_board_3 = [["o", "x", "o"], ["x", "o", "x"], ["o", "x", "o"]]

    assert tic_tac_toe_checker(test_board_3) == "o wins!"


def test_draw():
    """Testing that board is full of values"""
    test_board_4 = [["o", "x", "o"], ["x", "x", "o"], ["o", "o", "x"]]

    assert tic_tac_toe_checker(test_board_4) == "draw!"


def test_game_not_finished_yet():
    """Testing that"""
    test_board_5 = [["o", "x", "o"], ["x", "x", "o"], ["o", "o", "-"]]

    assert tic_tac_toe_checker(test_board_5) == "unfinished"
