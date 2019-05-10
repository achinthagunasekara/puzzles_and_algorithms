#!/usr/bin/python

"""
Solution to Find Angle Between Hour and Minute Hand Puzzle.
"""

from __future__ import print_function
import re


def run():
    """
    Get user input, process and return output.
    """
    while True:
        user_input = raw_input("Please enter the time in hh:mm format: ")
        print("Is this what you just said? ", user_input)
        if user_input.to_lower() == 'exit':
            break
        pattern = re.compile("^[1]*[1-9]:[0-5][0-9]$")
        if not pattern.match(user_input):
            print("Invalud input")
            continue


if __name__ == '__main__':
    run()
