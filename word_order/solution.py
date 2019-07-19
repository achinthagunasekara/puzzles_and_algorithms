#!/usr/local/bin/python3

"""
Solution to word order puzzle.
"""


def check_input(user_input):
    """
    Check input for the word end.
    If end present raise a KeyboardInterrupt and kill the program.
    Args:
        user_input (str): Input from the user.
    """
    if user_input.lower() == 'end':
        raise KeyboardInterrupt()
    return user_input


def get_user_input():
    """
    Get input from the user.
    Returns:
        list: List of strings.
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


def run():
    """
    Run the puzzle.
    """
    try:
        while True:
            words = get_user_input()
            if not words:
                pass
    except KeyboardInterrupt:
        print('Thank you for using this. Bye!')


if __name__ == '__main__':
    run()
