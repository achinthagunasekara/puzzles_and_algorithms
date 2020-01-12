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
    user_input = input('please enter the location: ')
    pattern = re.compile(r'^\([1-8] [1-8]\)\([1-8] [1-8]\)$')
    if not pattern.match(user_input):
        print('invalid input. please use the pattern (1 2)(5 2)')
        return get_user_input()
    return user_input

if __name__ == '__main__':
    print(get_user_input())
