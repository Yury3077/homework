"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def backspace_compare(first: str, second: str) -> bool:
    """
    Function that compare two str with symbol "#" means a backspace
    param:
        first (str): input string
        second(str) : input string
    return: True is strings are equal and False if not
    """
    if str_without_backspace(first) == str_without_backspace(second):
        return True
    else:
        return False


def str_without_backspace(some_str: str) -> str:
    """
    Find symbol "#" in str and delete previous letter in string
    param: some_str (str): input string
    return: String without "#"
    """
    str_without_backspace_1 = ""
    for symbol in some_str:
        if symbol == "#":
            str_without_backspace_1 = str_without_backspace_1[
                0 : len(str_without_backspace_1) - 1
            ]
        else:
            str_without_backspace_1 = str_without_backspace_1 + symbol
    return str_without_backspace_1


if __name__ == "__main__":
    t = backspace_compare("wet##c", "we#c")
    print(t)
