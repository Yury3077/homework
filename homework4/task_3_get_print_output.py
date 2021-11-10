"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.


my_precious_logger("error: file not found")
# stderr
'error: file not found'


my_precious_logger("OK")
# stdout
'OK'

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests

You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout
"""
import sys


def my_precious_logger(text: str) -> None:
    """
    Function that will receive a string and write it to stderr
    if line starts with "error" and to the stdout otherwise
        param: string with information
        return: None
    """
    if "error" in text.strip():
        sys.stderr.write(text + "\n")
    else:
        sys.stdout.write(text + "\n")


if __name__ == "__main__":
    my_precious_logger("error: file not found")
    my_precious_logger("OK")
