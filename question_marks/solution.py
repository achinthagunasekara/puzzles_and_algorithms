#!/usr/local/bin/python3

"""
Solution to question marks puzzle.
"""

from __future__ import print_function

def get_input():
    """
    Get input from the user.
    Returns.
        str: User input string.
    """
    while True:
        user_input = raw_input('Please enter your input: ')
        if user_input.lower() == 'end':
            return
        yield user_input


def check_questions_marks(string):
    """
    Check if there is are 3 question marks between two numbers
    that adds up to 10.
    Args:
        string (str): Input string to check.
    Returns:
        bool: True if string matches above condition, False otherwise.
    """
    pass


def run():
    """
    Run the puzzle.
    """
    for user_input in get_input():
        print(check_questions_marks(string=user_input))


if __name__ == '__main__':
    run()
