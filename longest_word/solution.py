#!/usr/bin/python

"""
Solution to longest word puzzle.
"""

from __future__ import print_function
import re


def check_for_longest_word(sentence):
    """
    Find the longest word in a given sentence.
    Args:
        sentence (str): Sentence to find the longest word in.
    Returns:
        str: Longest word in the given sentence.
    """
    pattern = re.compile("[a-zA-Z]+")
    result = pattern.findall(sentence)
    return max(result, key=len) if result else None


def run():
    """
    Get user input, process and return output.
    """
    print('Welcome. Please enter your sentence to find the longest word. Enter `exit` to end.')
    try:
        while True:
            user_input = raw_input("Please enter a sentence: ")

            if user_input.lower() == 'exit':
                break

            longest_word = check_for_longest_word(sentence=user_input)
            if not longest_word:
                print("No words were found in the input string")
            else:
                print(longest_word)

    except KeyboardInterrupt:
        print('\nThanks for using this program. Good bye!')


if __name__ == '__main__':
    run()
