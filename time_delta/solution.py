#!/usr/bin/python
"""
Solution to time delta puzzle.
"""

from __future__ import print_function


def get_test_cases():
    """
    Get input from the user.
    Returns.
        str: User input string.
    """
    test_cases = []
    number_of_test_cases = input('Please enter number of test cases: ')
    while number_of_test_cases > 0:
        test_case = raw_input("Please enter the test case {0}: ".format(number_of_test_cases))
        test_cases.append(test_case)
        number_of_test_cases -= 1
    return test_cases


def run():
    """
    Run function for the puzzle.
    """
    test_cases = get_test_cases()
    print(test_cases)


if __name__ == '__main__':
    run()
