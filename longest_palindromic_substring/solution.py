"""
Solution to longest palindromic substring puzzle.
"""

import logging


def find_longest_palindromic_substr(string):
    """
    Find the longest palindromic substring.
    Args:
        string (str): String to search for palindromic substrings.
    Returns:
        str: Logest palindromic substring in the given string.
    """
    logger = logging.getLogger('solution.find_longest_palindromic_substr')
    logger.info("Provided string is %s", string)


INPUTS = [
    'abwesdabcdeffedcbaaddsd'
]


if __name__ == '__main__':
    for each_input in INPUTS:
        print find_longest_palindromic_substr(string=each_input)
