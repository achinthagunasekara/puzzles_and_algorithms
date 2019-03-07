"""
Solution - Perform division of two numbers without using division operator (/).
"""


from __future__ import print_function


def devide(first, second):
    """
    Devide 2 numbers without using (/) operator.
    Args:
        first (int): First integer.
        second (int): Second integer.
    Returns:
         None
    """
    if second == 0:
        raise ZeroDivisionError("Unable to devide by zero ({0}/{1})".format(first, second))

    sign = bool((first * second) >= 0)
    first = abs(first)
    second = abs(second)
    quotient = 0

    while first >= second:
        first = first - second
        quotient += 1

    if not sign:
        quotient = -quotient
        first = -first

    print("Answer is {0} and {1}/{2}".format(quotient, first, second))


TESTS = [
    (1, 2),
    (20, 5),
    (60, -15),
    (100, 1000),
    (2, 0),
    (2, -3),
    (25, 4),
]


if __name__ == '__main__':
    for test in TESTS:
        try:
            devide(first=test[0], second=test[1])
        except ZeroDivisionError as zex:
            print(zex.message)
