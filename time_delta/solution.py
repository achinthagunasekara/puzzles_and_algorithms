#!/usr/bin/python
"""
Solution to time delta puzzle.
"""

from __future__ import print_function

def validate_date_time_input(datetime):
    """
    validate input datetime from the user.
    Args:
        datetime (str): input string from the user.
    Returns:
        datetime: datetime object.
    """
    pass



def get_test_cases():
    """
    Get input from the user.
    Returns.
        str: User input string.
    """
    test_cases = []
    number_of_test_cases = input('Please enter number of test cases: ')
    count = 0
    while number_of_test_cases > count:
        count += 1
        test_case = raw_input("Please enter the test case {0}: ".format(count))
        test_cases.append(test_case)
    return test_cases


def run():
    """
    Run function for the puzzle.
    """
    test_cases = get_test_cases()
    print(test_cases)


if __name__ == '__main__':
    run()
