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
    pos1 = list(map(int, user_inputs.group(1).split(' ')))
    pos2 = list(map(int, user_inputs.group(2).split(' ')))
    return pos1, pos2


def print_chess_board(pos1, pos2):
    """
    Print the chess board  and show where the pieces are.
    """
    for row in range(1, 9):
        row_graphic = ""
        for col in range(1, 9):
            #print("Pos_G {0}".format(pos1))
            #print("Pos_C ({0} {1})".format(row, col))
            if (pos1[0] == row and pos1[1] == col) or (pos2[0] == row and pos2[1] == col):
                row_graphic = "{0} X".format(row_graphic)
            else:
                row_graphic = "{0} ▇".format(row_graphic)
        print(row_graphic)


def calculate_paths(pos1, pos2):
    """
    Calculate paths from pos1 to pos2.
    """


def run():
    """
    Run the puzzle.
    """
    pos1, pos2 = get_user_input()
    print_chess_board(pos1=pos1, pos2=pos2)


if __name__ == '__main__':
    run()
