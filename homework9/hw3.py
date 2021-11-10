"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

# For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
# 6
# >>> universal_file_counter(test_dir, "txt", str.split)
# 6

"""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """
    Function that takes directory path, a file extension and an optional tokenizer.
    It will count lines in all files with that extension if there are no tokenizer.
    If a the tokenizer is not none, it will count tokens.
    param:
        dir_path: path of a directory
        file_extension: extension that we use in function
    return: number of lines in files with such extension
    """
    line_counter = 0
    file_list = os.listdir(path=dir_path)
    for file_name in file_list:
        if file_extension in file_name:
            file_path = os.path.join(dir_path, file_name)
            with open(file_path, "r") as fl:
                for line in fl:
                    str_line = line.strip()
                    if tokenizer:
                        list_after_tokenize = tokenizer(str_line)
                        line_counter += len(list_after_tokenize)
                    elif not tokenizer:
                        line_counter += 1
    return line_counter


if __name__ == "__main__":
    path = os.path.join(os.getcwd())
    print(path)
    print(universal_file_counter(path, "txt", str.split))
