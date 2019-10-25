#!/usr/local/bin/python3

"""
Solution to Closest Enemy Puzzle.
"""


class ClosestEnemyException(Exception):
    """
    Simple exception for this puzzle.
    """


def build_metrix():
    """
    Get input from the user and build a metrix.
    Returns:
        List: List of lists (metrix).
    """
    items_per_line = None
    metrix = []

    while True:
        user_input = input("Please enter the metric line {0}: ".format(len(metrix)))
        if user_input.lower() == 'end':
            return metrix

        user_input = user_input.split(' ')

        # items_per_line is only set once at the start.
        if not items_per_line:
            items_per_line = len(user_input)

        if items_per_line != len(user_input):
            raise ClosestEnemyException(
                "Input {0} has less or more than {1} items".format(user_input, items_per_line)
            )

        for item in user_input:
            if item not in ["0", "1", "2"]:
                raise ClosestEnemyException(
                    "Invalid input {0}. Must be one of 0, 1 or 2".format(item)
                )
        metrix.append(user_input)
    return metrix


if __name__ == '__main__':
    try:
        build_metrix()
    except ClosestEnemyException as ex:
        print("Something went wrong - {0}".format(ex))
