"""
Find numbers represented as sum of two cubes for two different pairs - Techie Delight.
"""


def find_two_cubes(integer):
    """
    Find numbers represented as sum of two cubes for two different pairs.
    Args:
        integer (int): Integer given to break into two cubes.
    Returns:
        tuple: Two integers who's cubes will make up the orginal integer.
    """
    pass


TEST_CASES = [
    1729,
    4104,
    13832,
    20683
]


if __name__ == '__main__':
    for test_case in TEST_CASES:
        print("{0} ==> {1}".format(test_case, find_two_cubes(integer=test_case)))
