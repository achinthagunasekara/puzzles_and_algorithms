#!/usr/bin/python

"""
Solution to Find Angle Between Hour and Minute Hand Puzzle.
"""

from __future__ import print_function
import re


def calculate(user_input):
    """
    Calculate the angle between hour and minute hand.
    Args:
        user_input (str): Input from the user.
    Returns:
        int: Angle between hour and minute hand.
    """
    user_input_list = user_input.split(':')
    print(user_input_list)


def run():
    """
    Get user input, process and return output.
    """
    print('Welcome. Please enter time in hh:mm format or exit to end the program')
    while True:
        user_input = raw_input("Please enter the time: ")

        if user_input.lower() == 'exit':
            break

        pattern = re.compile("^[1]*[1-9]:[0-5][0-9]$")
        if not pattern.match(user_input):
            print("Invalid input. Please try again")
            continue

        calculate(user_input)


if __name__ == '__main__':
    run()
