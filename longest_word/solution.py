#!/usr/bin/python

"""
Solution to longest word puzzle.
"""

from __future__ import print_function


def run():
    """
    Get user input, process and return output.
    """
    print('Welcome. Please enter your sentence to find the longest word. Enter `exit` to end.')
    try:
        while True:
            user_input = raw_input("Please enter the time: ")

            if user_input.lower() == 'exit':
                break

            print(user_input)

    except KeyboardInterrupt:
        print('\nThanks for using this program. Good bye!')


if __name__ == '__main__':
    run()
