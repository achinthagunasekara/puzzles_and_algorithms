"""
Solution to draw a rocket puzzle.
"""


# pylint: disable=superfluous-parens


def draw(word):
    """
    Draw the rocket with a word.
    Args:
        word (str): String to draw on the rocket.
    Returns:
        None
    """
    print('  |')
    print(' /_\\')
    print(' |I|')
    print(' |N|')
    print(' |D|')
    print(' |I|')
    print(' |A|')
    print(' |_|')
    print('/___\\')
    print(' VvV')


INPUTS = [
    '',
    'A',
    'SPACE'
]


if __name__ == '__main__':
    for each_word in INPUTS:
        draw(word=each_word)
