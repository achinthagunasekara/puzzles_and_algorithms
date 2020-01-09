#!/usr/local/bin/python3

"""
Solution.
"""

import re

def get_user_input():
    """
    Get the input from the user.
    Returns:
        string: Location of the chess board space.
    """
    user_input = input('Please enter the location: ')
    pattern = re.compile("^\([1-8] [1-8]\)\([1-8] [1-8]\)$")
    print(pattern.match(user_input))
    return user_input

if __name__ == '__main__':
    print(get_user_input())
