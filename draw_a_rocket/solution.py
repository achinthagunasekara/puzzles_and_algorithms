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
    word = list(word)
    print('  |')
    print(' /_\\')
    for each_letter in word:
        print(' |{0}|'.format(each_letter))
    print(' |_|')
    print('/___\\')
    print(' VvV\n\n')


INPUTS = [
    '',
    'A',
    'SPACE'
]


if __name__ == '__main__':
    for each_word in INPUTS:
        draw(word=each_word)
