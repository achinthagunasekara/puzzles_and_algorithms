"""
Solution to the correct path puzzle.
"""


from copy import copy


def get_grid():
    """
    Return the grid.
    Args:
    Returns:
        list: Grid structure.
    """
    row = ['0' for x_axis in range(0, 5)]  # pylint: disable=unused-variable
    grid = [copy(row) for y_axis in range(0, 5)]  # pylint: disable=unused-variable
    grid[0][0] = 'X'
    grid[4][4] = 'X'
    return grid


def print_grid(grid):
    """
    Print the grid on screen.
    Args:
        grid (list): Grid structure.
    Returns:
        None
    """
    for row in grid:
        print(' '.join(row))  # pylint: disable=superfluous-parens


def get_correct_path(path):
    """
    Returns the correct path for a given string.
    Args:
        path (str): Incomplete path string
    Rerutns:
        str: Complete path
    """
    grid = get_grid()
    print_grid(grid=grid)
    return path


INPUTS = [
    '???rrurdr?',
    'drdr??rrddd?'
]


if __name__ == '__main__':
    for each in INPUTS:
        print("{0} ==> {1}".format(each, get_correct_path(path=each)))  # pylint: disable=superfluous-parens
