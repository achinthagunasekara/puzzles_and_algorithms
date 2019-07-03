#!/usr/local/bin/python3
"""
Solution to time delta puzzle.
"""

from __future__ import print_function
from datetime import datetime


def get_datetime_input():
    """
    validate input datetime from the user.
    Args:
        (input_str) (str): input string from the user.
    Returns:
        datetime: datetime object.
    """
    datetime_str = input("Please enter a datetime string: ")
    datetime_object = None
    try:
        datetime_object = datetime.strptime(datetime_str, '%a %d %b %Y %H:%M:%S %z')
    except ValueError as val_err:
        print("Input error - {0}".format(val_err))
        get_datetime_input()
    return datetime_object


def get_test_cases():
    """
    Get input from the user.
    Returns.
        str: User input string.
    """
    test_cases = []

    try:
        number_of_test_cases = int(input('Please enter number of test cases: '))
    except ValueError:
        print('Error - Invalid number of test cases')
        return None

    count = 1
    while number_of_test_cases >= count:
        print("Test Case {0}".format(count))
        test_cases.append(
            (get_datetime_input(), get_datetime_input())
        )
        count += 1
    return test_cases


def process(test_cases):
    """
    Processes collected test cases.
    Args:
        test_cases (list): List of test cases
    """
    for test_case in test_cases:
        print(test_case)


def run():
    """
    Run function for the puzzle.
    """
    try:
        test_cases = get_test_cases()
        if test_cases:
            process(test_cases=test_cases)
    except KeyboardInterrupt:
        print('Thank you for using this program. Good bye!')


if __name__ == '__main__':
    run()
