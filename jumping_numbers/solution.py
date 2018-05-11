"""
Find jumping numbers.
"""


def get_jumping_numbers(input_int):
    """ Get jumping numbers """
    for each_int in range(input_int):
        print each_int


if __name__ == '__main__':
    INPUT = [
        10
    ]
    for integer in INPUT:
        print get_jumping_numbers(input_int=integer)
        print '======'
