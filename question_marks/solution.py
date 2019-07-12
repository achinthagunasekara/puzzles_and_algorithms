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


def run():
    """
    Run the puzzle.
    """
    user_input = get_input()


if __name__ == '__main__':
    run()
