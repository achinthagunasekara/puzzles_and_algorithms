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


def print_the_square(words):
    """
    Print the square.
    Args:
        words (list): List of words.
    """
    for word in words:
        print(word)


def vowel_square(words):
    """
    Do the thing.
    Args:
        words (list): List of strings entered by the user.
    """
    for index_row, row in enumerate(words):
        for index_letter, letter in enumerate(row):
            if not letter in VOWELS:
                continue
            try:
                if not row[index_letter + 1] in VOWELS:
                    continue
            except IndexError:
                continue

            try:
                if not words[index_row + 1][index_letter] in VOWELS:
                    continue
            except IndexError:
                continue

            try:
                if not words[index_row + 1][index_letter + 1] in VOWELS:
                    continue
            except IndexError:
                continue

            return (index_row, index_letter)


def run():
    """
    Run the puzzle.
    """
    words = get_user_input()
    print_the_square(words=words)
    pos = vowel_square(words=words)
    if pos:
        print("Vowel square starts at {0}".format(pos))
    else:
        print('Vowel square not found')


if __name__ == '__main__':
    run()
