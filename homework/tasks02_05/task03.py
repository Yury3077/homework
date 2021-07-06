"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
import math
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    read a file line by line that consists of str
    str include numbers (separated with commas)
    :param file_name: name of file + .txt
    :return: min_value, max_value in file
    """
    min_num = math.inf
    max_num = -math.inf
    with open(file_name) as fi:
        for line in fi:
            line_split = line.split(",")
            for char in line_split:
                char = int(char)
                if char <= min_num:
                    min_num = char
                if char >= max_num:
                    max_num = char
    result_tuple = (min_num, max_num)

    return result_tuple