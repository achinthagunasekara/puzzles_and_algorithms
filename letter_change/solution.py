#!/usr/bin/python

"""
Solution to letter change puzzle.
"""

from __future__ import print_function
import string


VOWELS = ['a', 'e', 'i', 'o', 'u']
LETTERS = string.ascii_lowercase[:26]

def get_input():
    """
    Get input from the user.
    Returns.
        str: User input string.
    """
    while True:
        user_input = raw_input('Please enter a sentence: ')
        if user_input.lower() == 'end':
            return
        yield user_input

def change_letters(sentence):
    """
    Change letters in the given string.
    Args:
        sentence (str): Input string.
    Returns:
        str: Changed string.
    """
    changed = []
    for letter in sentence:
        upper = letter.isupper()
        try:
            current_letter_index = LETTERS.index(letter.lower())
            changed_letter_index = current_letter_index + 1
            changed_letter = LETTERS[changed_letter_index]
        except IndexError: # letter must be z
            changed_letter = LETTERS[0]
        except ValueError: # letter must not be in [a-z]
            changed_letter = letter

        changed_letter = changed_letter.upper() if upper else changed_letter
        changed.append(changed_letter)
    return ''.join(changed)


if __name__ == '__main__':
    try:
        for each_input in get_input():
            print("'{0}' can be encoded to '{1}'".format(
                each_input, change_letters(sentence=each_input)
            ))
    except KeyboardInterrupt:
        pass
    print('Thank you for using letter change script!')
