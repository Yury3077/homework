import os

from homework.Tasks02_05.task03 import find_maximum_and_minimum


def test_find_maximum_and_minimum_in_file_with_nums():
    """Testing that function find min and max in file"""
    text_file = open("text_with_nums.txt", "w")
    text_file.write("1,2,3,5,613")
    text_file.close()
    path_dir = os.getcwd()
    assert find_maximum_and_minimum(os.path.join(path_dir, "text_with_nums.txt")) == [
        (1, 613)
    ]
    os.remove(os.path.join(path_dir, "text_with_nums.txt"))
