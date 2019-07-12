#!/usr/local/bin/python3

"""
Solution to question marks puzzle.
"""

from __future__ import print_function

def get_input():
    """
    Get input from the user.
    Returns.
        str: User input string.
    """
    while True:
        user_input = input('Please enter your input: ')
        if user_input.lower() == 'end':
            return
        yield user_input


def check_questions_marks(string):
    """
    Check if there is are 3 question marks between two numbers
    that adds up to 10.
    Args:
        string (str): Input string to check.
    Returns:
        bool: True if string matches above condition, False otherwise.
    """
    num_of_question_marks = 0
    index_checking_from = None
    for index, char in enumerate(string):
        if char.isdigit():
            index_checking_from = index

            if num_of_question_marks == 3:
                return True

            num_of_question_marks = 0

        if index_checking_from is not None and char == "?":
            num_of_question_marks += 1
    return False


def run():
    """
    Run the puzzle.
    """
    try:
        for user_input in get_input():
            print(check_questions_marks(string=user_input))
    except KeyboardInterrupt:
        pass
    print('Thank you for using. Good bye!')


if __name__ == '__main__':
    run()
