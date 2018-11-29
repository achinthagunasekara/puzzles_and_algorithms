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
    grid = []
    for y_axis in range(0, 5):
        for x_axis in range(0, 5):
            grid[y_axis][x_axis] = 0
    print grid
    return path


INPUTS = [
    '???rrurdr?',
    'drdr??rrddd?'
]


if __name__ == '__main__':
    for each in INPUTS:
        print("{0} ==> {1}".format(each, get_correct_path(path=each)))  # pylint: disable=superfluous-parens
