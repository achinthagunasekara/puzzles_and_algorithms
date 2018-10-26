"""
Find numbers represented as sum of two cubes for two different pairs - Techie Delight.
"""


def is_cube(integer):
    """
    Check if a given integer is a prefect cube of something.
    Args:
        integer: Number to check if it's a cube.
    Returns:
        int: Cube root of the number. If not a prefect cube, this will return None.
    """
    cube_root = integer ** (1./3.)
    if round(cube_root) ** 3 == integer:
        return cube_root
    return None


def find_two_cubes(integer):
    """
    Find numbers represented as sum of two cubes for two different pairs.
    Args:
        integer (int): Integer given to break into two cubes.
    Returns:
        tuple: Two integers who's cubes will make up the orginal integer.
    """
    for first_part in range(integer):
        print first_part


TEST_CASES = [
    1729,
    #4104,
    #13832,
    #20683
]


if __name__ == '__main__':
    for test_case in TEST_CASES:
        print("{0} ==> {1}".format(test_case, find_two_cubes(integer=test_case)))
