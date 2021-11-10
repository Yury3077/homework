"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

"""
from typing import Generator, Iterator, List


def create_iter(file_name: str) -> Generator:
    """
    Function create a generator from file
    """
    with open(file_name, "r") as fl:
        for line in fl:
            str_line = line.strip()
            yield int(str_line)


def merge_sorted_files(file_list: List[str]) -> Iterator:
    """
    Create an iterator in order to merge list of data files
    param:
        file_list: list of path to files
    return:
        iterator that return a values from files in a queue

    >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    list_generators = []
    for file_number in range(len(file_list)):
        list_generators.append(create_iter(file_list[file_number]))
    while True:
        try:
            for value in list_generators:
                yield next(value)
        except StopIteration:
            break


if __name__ == "__main__":
    t = merge_sorted_files(["file1.txt", "file2.txt"])
    # for i in t:
    #     print(i)
    # print(dir(t))
    print(list(t))
