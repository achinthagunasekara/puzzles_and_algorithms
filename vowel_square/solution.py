#!/usr/local/bin/python3
"""
Solution to vowel square puzzle.
"""

VOWELS = ['a', 'e', 'i', 'o', 'u']

def get_user_input():
    """
    Get input from the user.
    """
    words = input('Please enter a comma seperated list of words: ')
    return words.replace(' ', '').split(',')


def run():
    """
    Run the puzzle.
    """
    words = get_user_input()
    print(words)


if __name__ == '__main__':
    run()
