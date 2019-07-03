#!/usr/local/bin/python3
"""
Solution to time delta puzzle.
"""

from __future__ import print_function
from datetime import datetime


def validate_date_time_input(input_str):
    """
    validate input datetime from the user.
    Args:
        (input_str) (str): input string from the user.
    Returns:
        datetime: datetime object.
    """
    datetime_object = None
    try:
        datetime_object = datetime.strptime(input_str, '%a %d %b %Y %H:%M:%S %z')
    except ValueError as val_err:
        print("Input error - {0}".format(val_err))
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
        print('Please enter a vaild number for number of test cases')
        return None

    count = 1
    while number_of_test_cases >= count:
        test_case = input("Please enter the test case {0}: ".format(count))
        test_case = validate_date_time_input(input_str=test_case)
        if not test_case:
            print('Looks like your input is invalid. Please try again')
        else:
            test_cases.append(test_case)
            count += 1
    return test_cases


def run():
    """
    Run function for the puzzle.
    """
    try:
        test_cases = get_test_cases()
        print(test_cases)
    except KeyboardInterrupt:
        print('Thank you for using this program. Good bye!')


if __name__ == '__main__':
    run()
