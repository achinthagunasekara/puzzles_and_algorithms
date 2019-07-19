#!/usr/local/bin/python3

"""
Solution to word order puzzle.
"""

def get_user_input():
    """
    Get input from the user.
    """
    words = []
    num_words = input("Enter the number of words you want to input: ")
    try:
        num_words = int(num_words)
    except ValueError:
        print('Please enter a valid integer')
        return None

    for iteration in range(num_words):
        words.append(input("Please enter the word {0}: ".format(iteration + 1)))

    return words



if __name__ == '__main__':
    get_user_input()
