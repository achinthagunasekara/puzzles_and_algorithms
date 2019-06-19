"""
Solution to letter change puzzle.
"""

from __future__ import print_function

def get_input():
    """
    Get input from the user.
    Returns.
        str: User input string.
    """
    while True:
        user_input = raw_input("Please enter a sentence: ")
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

if __name__ == '__main__':
    for each_input in get_input():
        print(change_letters(sentence=each_input))
