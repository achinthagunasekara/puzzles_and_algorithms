"""
Given a string consisting of opening and closing parenthesis,
find length of the longest valid parenthesis substring.
"""


def find_parenthesis(string):
    """
    Find opening and closing parenthesis.
    Args:
        string (string): Input string to sarch in.
    Returns:
        string: Cleaned up version of the input string.
    """
    output = ''
    str_list = string.split(')')
    for index, element in enumerate(str_list):
        if element:
            open_count = element.count('(')
            close_count = 1
            next_index = index + 1
            while next_index < (len(str_list) - 1) and str_list[next_index] == '':
                close_count += 1
                next_index += 1

            min_num_of_parenthesis = min(open_count, close_count)

            for num in range(min_num_of_parenthesis):  # pylint: disable=unused-variable
                output = "%s(" % output

            for num in range(min_num_of_parenthesis):  # pylint: disable=unused-variable
                output = "%s)" % output
    return output


INPUTS = [
    '((()',
    ')()())',
    '()(()))))'
]

for each_input in INPUTS:
    print "%s ==> %s" % (each_input, find_parenthesis(each_input))
    print "========"
