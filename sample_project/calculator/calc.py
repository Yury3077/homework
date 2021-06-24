"""
Task01 from homework1: fix all bugs in the `sample_project` code

"""


def check_power_of_2(a: int) -> bool:
    """
    Checking number is it power of 2
    :param a: integer
    :return: True/False
    """

    return not (bool(a == 0 or (a & (a - 1))))

print(check_power_of_2(-1))