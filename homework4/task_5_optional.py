"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


# >>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator, List


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """
    A generator that takes a number N as an input and yields N FizzBuzz numbers
        param: number of last value from generator
        yield: value of fizzbuzz game
    """
    counter = 1
    while counter <= n:
        yield "Fizz" * (not counter % 3) + "Buzz" * (not counter % 5) or str(counter)
        counter += 1


if __name__ == "__main__":
    t = fizzbuzz(20)
    print(list(t))
