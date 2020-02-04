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
    user_inputs = re.search(r'\((.*)\)\((.*)\)', user_input)
    print(user_inputs.group(2))
    return user_input


def print_chess_board():
    """
    Print the chess board  and show where the pieces are
    """
    for _ in range(0, 8):
        row = ""
        for _ in range(0, 8):
            row = "{0} ▇".format(row)
        print(row)


if __name__ == '__main__':
    get_user_input()
    print_chess_board()
