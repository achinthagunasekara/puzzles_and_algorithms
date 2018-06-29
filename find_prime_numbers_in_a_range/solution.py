"""
Solution to `Find Prime numbers in a range` puzzle.
"""

def check_if_prime_number(number, known_prime_numers):
    """
    Check if a number is a prime number. Also pass in a list of,
    known prime numbers for a speedy lookup.
    Args:
        number (int): Number to check if it's a prime number.
        known_prime_numbers (list): List of known prime numbers.
    Returns:
        bool: True if a prime number. False if not.
    """
    if number in known_prime_numers:
        return True

    for each_number in range(2, number):
        if not number % each_number:
            return False
    known_prime_numers.append(number)
    return True


INPUT = [
    (1, 10),
    (3, 5),
    (1, 10000),
]

if __name__ == '__main__':
    known_prime_numbers = []  # pylint: disable=invalid-name
    for each_pair in INPUT:
        prime_numbers = []
        for each_int in range(each_pair[0], each_pair[1] + 1):
            if check_if_prime_number(each_int, known_prime_numbers):
                prime_numbers.append(each_int)
        print ' '.join(map(str, prime_numbers))
