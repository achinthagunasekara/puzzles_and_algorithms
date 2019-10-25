#!/usr/local/bin/python3

"""
Solution to Closest Enemy Puzzle.
"""


class ClosestEnemyException(Exception):
    """
    Simple exception for this puzzle.
    """
    pass


def get_input(line):
    """
    Get input  from the user.
    Args:
        line (int): Line number that's been collected.
    Returns:
        List: List of collected values.
    """
    inputs = input("Please enter the metric {0}".format(line)).split(" ")
    for each_input in inputs:
        if each_input not in ["0", "1", "2"]:
            raise ClosestEnemyException(
                "Invalid input {0}. Must be one of 0, 1 or 2".format(each_input)
            )
    return inputs

def build_metrix():
    """
    Get input from the user and build the metrix.
    Returns:
        List: 2D matrix with the layout.
    """
    rows = 0
    cols = 0
    get_input(0)

if __name__ == '__main__':
    build_metrix()
