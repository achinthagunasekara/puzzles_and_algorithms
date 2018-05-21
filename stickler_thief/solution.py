""" Solution to stickler thief puzzle """


def get_max_loot(input_list):
    """
    Get the maximum amount of loot the thief can collect.
    Args:
        input_list (list): Input list of houses.
    Returns:
        int: Value of the total loot.
    """
    even = sum(input_list[::2])
    odd = sum(input_list[1::2])
    return even if even > odd else odd


if __name__ == '__main__':
    INPUT = [
        [5, 5, 10, 100, 10, 5],
        [1, 2, 3]
    ]
    for each_list in INPUT:
        print get_max_loot(input_list=each_list)
