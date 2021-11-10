"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Function that takes a number N as an input and returns N FizzBuzz numbers,
    whole division on 3 and 5
        param: number, last number for checking
        return: list with str values
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(10)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz']
    """
    list_res = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            list_res.append("fizz")
        elif i % 5 == 0:
            list_res.append("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            list_res.append("fizz buzz")
        else:
            list_res.append(str(i))
    return list_res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
