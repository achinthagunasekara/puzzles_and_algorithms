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
    for index_outter, each_outter_letter in enumerate(str_list):  # pylint: disable=unused-variable
        temp_list = []
        sliced_str_list = str_list[index_outter:]
        for index_inner, each_inner_letter in enumerate(sliced_str_list):
            temp_list.append(each_inner_letter)
            num_items_in_tmp = len(temp_list)
            next_even_list = sliced_str_list[index_inner + 1:index_inner + 1 + num_items_in_tmp]
            next_even_list.reverse()
            if temp_list == next_even_list:
                palindromes.append(
                    str_list[index_outter:index_outter + index_inner + num_items_in_tmp + 1]
                )
            next_odd_list = sliced_str_list[index_inner + 2:index_inner + 2 + num_items_in_tmp]
            next_odd_list.reverse()
            if temp_list == next_odd_list:
                palindromes.append(
                    str_list[index_outter:index_outter + index_inner + num_items_in_tmp + 2]
                )
    return "".join(max(palindromes, key=len))


INPUTS = [
    'abwesdabcdeffedcbaaddsd',
    'abbaasua8723bgajag',
    '12345678abba12345678',
    '00000sssrader343434121',
    '0000sssradar343a4341a21'
]


if __name__ == '__main__':
    for each_input in INPUTS:
        logging.basicConfig(level=logging.INFO)
        print find_longest_palindromic_substr(string=each_input)
