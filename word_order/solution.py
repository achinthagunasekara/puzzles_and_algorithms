#!/usr/local/bin/python3

"""
Solution to word order puzzle.
"""

def get_user_input():
    """
    Get input from the user.
    """
    num_words = input("Enter the number of words you want to input: ")
    try:
        num_words = int(num_words)
    except ValueError:
        print('Please enter a valid integer')
        return

    for iteration in range(num_words):
        num_words = input("Please enter the word {0}: ".format(iteration + 1))


if __name__ == '__main__':
    get_user_input()
