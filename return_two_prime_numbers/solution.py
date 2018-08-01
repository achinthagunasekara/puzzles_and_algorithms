"""
Solution to return two prime numbers puzzle.
"""

from math import sqrt
from itertools import count, islice


PRIME_NUMBERS = []


def generate_prime_numbers(input_number):
    """
    Generate a list of prime numbers up to a given number.
    Args:
        input_number (int): Input number to generate prime numbers upto.
    Returns:
        None
    """
    for number in range(2, input_number):
        if number > 1 and all(number % i for i in islice(count(2), int(sqrt(number)-1))):
            PRIME_NUMBERS.append(number)


def get_prime_numbers(number):
    """
    Given an even number ( greater than 2 ),
    return two prime numbers whose sum will be equal to given number.
    There are several combinations possible.
    This function returns the first such pair.
    Args:
        number (int): Number given.
    Returns:
        list: List with two prime numbers that makes up the given number.
    """
    make_up_numbers = []
    for each_prime_number in PRIME_NUMBERS:
        remainder = number - each_prime_number
        if remainder in PRIME_NUMBERS:
            make_up_numbers = sorted([each_prime_number, remainder])
    return make_up_numbers


if __name__ == '__main__':
    INTEGERS = [
        74,
        1024,
        66,
        8,
        9990
    ]
    # Generate a list of prime numbers up to the larget number on the list.
    generate_prime_numbers(input_number=max(INTEGERS))
    for integer in INTEGERS:
        print get_prime_numbers(number=integer)
