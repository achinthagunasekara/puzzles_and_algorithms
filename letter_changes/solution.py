#!/usr/bin/env python
"""
Solution to letter change puzzle.
"""


from string import ascii_lowercase


def change_letters(input_string):
    """
    Change letters in a given string.
    Args:
        input_string (str): String to modify.
    Returns:
        str: Modified string.
    """
    modified_string = ""
    alphabet = list(ascii_lowercase)
    for each_char in input_string:
        is_uppercase = each_char.istitle()
        each_char = each_char.lower()
        if each_char in alphabet:
            try:
                each_char = alphabet[alphabet.index(each_char) + 1]
            except IndexError:
                each_char = alphabet[0]
        if is_uppercase:
            each_char = each_char.upper()
        modified_string = "{0}{1}".format(modified_string, each_char)
    return modified_string


STRINGS = [
    'hello*3',
    'fun times!',
    'Abcdz'
]


if __name__ == '__main__':
    for each_string in STRINGS:
        print "{0} ==> {1}".format(each_string, change_letters(input_string=each_string))
