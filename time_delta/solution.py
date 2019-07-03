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
    datetime_object = datetime.strptime(input_str, '%a %d %b %Y %H:%M:%S %z')
    return datetime_object



def get_test_cases():
    """
    Get input from the user.
    Returns.
        str: User input string.
    """
    test_cases = []
    number_of_test_cases = int(input('Please enter number of test cases: '))
    count = 0
    while number_of_test_cases > count:
        count += 1
        test_case = input("Please enter the test case {0}: ".format(count))
        test_cases.append(validate_date_time_input(input_str=test_case))
    return test_cases


def run():
    """
    Run function for the puzzle.
    """
    test_cases = get_test_cases()
    print(test_cases)


if __name__ == '__main__':
    run()
