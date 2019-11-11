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
    friendly_found = False
    metrix = []

    while True:
        user_input = input("Please enter the metric line {0}: ".format(len(metrix)))
        if user_input.lower() == 'end' or user_input == '':
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
            # In the whole metrix, value 1 is allowed once only.
            # If user enters more than 1 character, metrix is not valid.
            if item == "1":
                if friendly_found:
                    raise ClosestEnemyException('You can only enter one friendly (value 1)')
                friendly_found = True

        metrix.append(user_input)
    return metrix


def print_metrix(metrix):
    """
    Print the metrix in a pretty format.
    Args:
        metrix (list): List of lists (metrix).
    """
    for row in metrix:
        print(' '.join(row))


def get_friendly_pos(metrix):
    """
    Get the position of the friendly.
    Args:
        metrix (list): List of lists (metrix).
    Returns:
        tuple: Position of the friendly.
    """
    for col_index, col in enumerate(metrix):
        for row_index, row in enumerate(col):
            if row == '1':
                return (col_index, row_index)
    return None


def get_enemy_pos(metrix):
    """
    Get the enemy positions.
    Args:
        metrix (list): List of lists (metrix).
    Returns:
        list: List of tuples containing enemy positions.
    """
    enemies = []
    for col_index, col in enumerate(metrix):
        for row_index, row in enumerate(col):
            if row == '2':
                enemies.append((col_index, row_index))
    return enemies


def find_closest_enemy(metrix):
    """
    Find the closest enemy in a given metrix.
    Args:
        metrix (list): List of lists (metrix).
    Returns:
        tuple, int: Location of the enemy and and distance to it.
    """
    friendly_pos = get_friendly_pos(metrix=metrix)
    if not friendly_pos:
        raise ClosestEnemyException('No friendly found in the metrix')
    print("Friendly is located at {0}".format(friendly_pos))

    closest_enemy = None
    closest_dist = None
    for col_index, col in enumerate(metrix):
        for row_index, row in enumerate(col):
            if row == '2':
                enemy_pos = (col_index, row_index)
                dist = abs(friendly_pos[0] - enemy_pos[0]) + abs(friendly_pos[1] - enemy_pos[1])
                print("Enemy found at {0} and {1} jumps away".format(enemy_pos, dist))
                if not closest_enemy:
                    closest_enemy = enemy_pos
                    closest_dist = dist
                if closest_dist > dist:
                    closest_enemy = enemy_pos
                    closest_dist = dist
    return closest_enemy, closest_dist


def run():
    """
    Run the puzzle.
    """
    try:
        metrix = build_metrix()
        print_metrix(metrix=metrix)
        closest_enemy, closest_dist = find_closest_enemy(metrix=metrix)
        print("Closest enemy is {0} and {1} jumps away".format(closest_enemy, closest_dist))
    except ClosestEnemyException as ex:
        print("Something went wrong - {0}".format(ex))


if __name__ == '__main__':
    run()
