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
    words = words.replace(' ', '').split(',')

    iterator = iter(words)
    the_len = len(next(iterator))
    if not all(len(word) == the_len for word in words):
        print('All words must be of same length. Please try again')
        return get_user_input()

    return words


def run():
    """
    Run the puzzle.
    """
    words = get_user_input()
    print(words)


if __name__ == '__main__':
    run()
