#!/usr/bin/python

"""
Solution.
"""

def get_user_input():
    """
    Get the input from the user.
    Returns:
        string: Location of the chess board space.
    """
    user_input = input('Please enter the location: ')
    return user_input

if __name__ == '__main__':
    print(get_user_input())
