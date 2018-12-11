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
    row = ['O' for x_axis in range(0, 5)]  # pylint: disable=unused-variable
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


def shift_up(coordinates):
    """
    Shift up the given coordinates.
    Args:
        coordinates (list): List of coordinates.
    Returns:
        list: List of shifted coordinates.
    """
    for index, each_coordinate in enumerate(coordinates):
        if each_coordinate != '?':
            coordinates[index] = (each_coordinate[0] - 1, each_coordinate[1])


def shift_right(coordinates):
    """
    Shift right the given coordinates.
    Args:
        coordinates (list): List of coordinates.
    Returns:
        list: List of shifted coordinates.
    """
    for index, each_coordinate in enumerate(coordinates):
        if each_coordinate != '?':
            coordinates[index] = (each_coordinate[0], each_coordinate[1] + 1)


def shift_down(coordinates):
    """
    Shift down the given coordinates.
    Args:
        coordinates (list): List of coordinates.
    Returns:
        list: List of shifted coordinates.
    """
    for index, each_coordinate in enumerate(coordinates):
        if each_coordinate != '?':
            coordinates[index] = (each_coordinate[0] + 1, each_coordinate[1])
    print coordinates


def shift_left(coordinates):
    """
    Shift left the given coordinates.
    Args:
        coordinates (list): List of coordinates.
    Returns:
        list: List of shifted coordinates.
    """
    for index, each_coordinate in enumerate(coordinates):
        if each_coordinate != '?':
            coordinates[index] = (each_coordinate[0], each_coordinate[1] - 1)


def get_correct_path(path):
    """
    Returns the correct path for a given string.
    Args:
        path (str): Incomplete path string
    Rerutns:
        str: Complete path
    """
    start = (0, 1)
    end = (4, 4)
    coordinates = []
    coordinates.append(start)
    last_step = start

    grid = get_grid()
    print_grid(grid=grid)

    path = list(path)
    for each_step in path:
        if coordinates[-1] != '?':
            last_step = coordinates[-1]
        if each_step == 'u':
            if last_step[0] - 1 < 0:
                shift_down(coordinates)
                next_step = last_step
            else:
                next_step = (last_step[0] - 1, last_step[1])
        elif each_step == 'r':
            if last_step[1] + 1 > len(grid[0]) - 1:
                shift_left(coordinates)
                next_step = last_step
            else:
                next_step = (last_step[0], last_step[1] + 1)
        elif each_step == 'd':
            if last_step[0] + 1 > len(grid) - 1:
                shift_up(coordinates)
                next_step = last_step
            else:
                next_step = (last_step[0] + 1, last_step[1])
        elif each_step == 'l':
            if last_step[1] - 1 < 0:
                shift_right(coordinates)
                next_step = last_step
            else:
                next_step = (last_step[0], last_step[1] - 1)
        else:
            next_step = '?'
        coordinates.append(next_step)
    print coordinates
    return path


INPUTS = [
    '???rrurdr?',
    'drdr??rrddd?'
]


if __name__ == '__main__':
    for each in INPUTS:
        print("{0} ==> {1}\n".format(each, get_correct_path(path=each)))  # pylint: disable=superfluous-parens
