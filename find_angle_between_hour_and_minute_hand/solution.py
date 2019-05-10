#!/usr/bin/python

"""
Solution to Find Angle Between Hour and Minute Hand Puzzle.
"""

from __future__ import print_function
import re

def convert_hand_to_deg(position, hour_hand=False):
    """
    Convert hour hand position to deg.
    Args:
        position (int): Position of the hour hand.
    Returns:
        int: Deg of the hour hand.
    """
    devide = (12 if hour_hand else 60)
    each_hour = 360/devide
    return each_hour * position


def calculate(user_input):
    """
    Calculate the angle between hour and minute hand.
    Args:
        user_input (str): Input from the user.
    Returns:
        int: Angle between hour and minute hand.
    """
    user_input_list = [int(x) for x in user_input.split(':')]
    hour_deg = convert_hand_to_deg(position=user_input_list[0], hour_hand=True)
    minute_deg = convert_hand_to_deg(position=user_input_list[1])
    deg = 360 - abs(hour_deg - minute_deg)
    symbol = u'\xb0'.encode('utf8')
    print("{0}{1}".format(deg, symbol))


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

        calculate(user_input=user_input)


if __name__ == '__main__':
    run()
