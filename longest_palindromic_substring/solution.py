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
    palindromes = []
    logger.info("Provided string is %s", string)
    str_list = list(string)
    print str_list


INPUTS = [
    'abwesdabcdeffedcbaaddsd',
    'abbaasua8723bgajag',
    '12345678abba12345678'
]


if __name__ == '__main__':
    for each_input in INPUTS:
        logging.basicConfig(level=logging.INFO)
        print find_longest_palindromic_substr(string=each_input)
