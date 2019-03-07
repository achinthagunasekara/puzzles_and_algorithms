"""
Solution to Return 0, 1 and 2 with equal probability using the specified function puzzle.
"""


from __future__ import print_function
import random


def get_a_random():
    """
    Get a random 1 or 0.
    Returns:
        int: 1 or 0
    """
    return random.randint(0, 1)


def generate():
    """
    Return 0, 1 and 2 with equal probability using specified function.
    Returns:
        int: 0, 1 or 2.
    """
    first = get_a_random()
    second = get_a_random()

    return generate() if (first == 1 and second == 0) else (first + second)


def run():
    """
    Run the solution.
    """
    first = 0
    second = 0
    third = 0

    count = 0
    while count < 100000:
        count += 1
        val = generate()
        if val == 0:
            first += 1
        elif val == 1:
            second += 1
        else:
            third += 1
    print("0 ~ {0}, 1 ~ {1}, 2 ~ {2}".format(first, second, third))


if __name__ == '__main__':
    run()
