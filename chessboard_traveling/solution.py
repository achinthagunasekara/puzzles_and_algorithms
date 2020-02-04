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
    return user_inputs.group(1).split(' '), user_inputs.group(2).split(' ')


def print_chess_board(pos1, pos2):
    """
    Print the chess board  and show where the pieces are.
    """
    for _ in range(0, 8):
        row = ""
        for _ in range(0, 8):
            row = "{0} ▇".format(row)
        print(row)


def run():
    """
    Run the puzzle.
    """
    pos1, pos2 = get_user_input()
    print_chess_board(pos1=pos1, pos2=pos2)


if __name__ == '__main__':
    run()
