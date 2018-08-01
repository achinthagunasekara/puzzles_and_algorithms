"""
Solution to return two prime numbers puzzle.
"""

PRIME_NUMBERS = []

def get_prime_numbers(number):
    """
    Given an even number ( greater than 2 ),
    return two prime numbers whose sum will be equal to given number.
    There are several combinations possible.
    This function returns the first such pair.
    Args:
        number (int): Number given.
    Returns:
        tuple: Tuple with two prime numbers that makes up the given number.
    """
    return number

if __name__ == '__main__':
    INTEGERS = [
        5,
        74,
        1024,
        66,
        8,
        9990
    ]
    for integer in INTEGERS:
        print get_prime_numbers(number=integer)
