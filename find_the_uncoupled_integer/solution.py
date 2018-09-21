"""
Solution to Find the Uncoupled Integer puzzle.
"""


TEST_CASES = [
    '1, 2, 3, 1, 2',
    '1, 2, 3, 4, 5, 99, 1, 2, 3, 4, 5'
]


def find_the_uncoupled_integer(string):
    """
    Find the Uncoupled Integer in a given string.
    Args:
        string (str): Input string to process.
    Returns:
        int: Uncoupled integer.
    """
    return string


if __name__ == '__main__':
    for each_test_case in TEST_CASES:
        print find_the_uncoupled_integer(string=each_test_case)
