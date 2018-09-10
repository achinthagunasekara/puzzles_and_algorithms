#!/usr/bin/env python
"""
Solution to letter change puzzle.
"""


def change_letters(string):
    """
    Change letters in a given string.
    Args:
        string (str): String to modify.
    Returns:
        str: Modified string.
    """
    return string


STRINGS = [
    'hello*3',
    'fun times!'
]


if __name__ == '__main__':
    for each_string in STRINGS:
        print "{0} ==> {1}".format(each_string, change_letters(string=each_string))
