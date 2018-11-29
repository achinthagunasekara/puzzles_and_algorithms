"""
Solution to the correct path puzzle.
"""


def get_correct_path(path):
    """
    Returns the correct path for a given string.
    Args:
        path (str): Incomplete path string
    Rerutns:
        str: Complete path
    """
    row = [0 for x_axis in range(0, 5)]  # pylint: disable=unused-variable
    grid = [row for y_axis in range(0, 5)]  # pylint: disable=unused-variable
    print grid
    return path


INPUTS = [
    '???rrurdr?',
    'drdr??rrddd?'
]


if __name__ == '__main__':
    for each in INPUTS:
        print("{0} ==> {1}".format(each, get_correct_path(path=each)))  # pylint: disable=superfluous-parens
