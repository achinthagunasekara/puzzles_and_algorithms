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


def print_chess_board():
    """
    Print the chess board  and show where the pieces are
    """
    for row in range(0, 8):
        for col in range(0, 8):
            print(col)
        print('\n')


if __name__ == '__main__':
    #print(get_user_input())
    print_chess_board()
