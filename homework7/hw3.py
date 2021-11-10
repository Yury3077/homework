"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List

from homework7.hw1 import find_occurrences


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Checking a Tic-Tac-Toe 3x3 board
    If there is "x" winner, function should return "x wins!"
    If there is "o" winner, function should return "o wins!"
    If there is a draw, function should return "draw!"
    If board is unfinished, function should return "unfinished!"
    param:
        board (List[List]): input bord
    return: result str
    """
    for line in board:
        if len(set(line)) == 1:
            return f"{line[0][0]} wins!"

    for num in range(len(board)):
        list_column = []
        for row in range(len(board)):
            list_column.append(board[row][num])
            if len(list_column) == len(board) and len(set(list_column)) == 1:
                return f"{list_column[0]} wins!"

    list_diagonal = []
    for number in range(len(board)):
        list_diagonal.append(board[number][number])
    if len(set(list_diagonal)) == 1:
        return f"{list_diagonal[0]} wins!"

    list_diagonal_2 = []
    for row, pos in enumerate(range(2, -1, -1)):
        list_diagonal_2.append(board[row][pos])
    if len(set(list_diagonal_2)) == 1:
        return f"{list_diagonal_2[0]} wins!"

    if find_occurrences(board, "-") != 0:
        return "unfinished"
    else:
        return "draw!"


if __name__ == "__main__":
    t = tic_tac_toe_checker([["o", "x", "o"], ["x", "x", "o"], ["o", "o", "x"]])
    print(t)
