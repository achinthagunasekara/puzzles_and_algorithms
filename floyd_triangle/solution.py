"""
Solution to the Floyd Triangle puzzle.
"""


def get_user_input():
    """
    Get input from the user.
    Args:
    Returns:
        int: Number entered by the user.
    """
    user_input = raw_input('Please enter the number of rows: ')
    try:
        return int(user_input)
    except ValueError:
        print('Sorry, you have entered an invalid value')


def print_traingle(number):
    """
    Print the Floydt raingle using the number entered by the user.
    Args:
        number (int): Number entered by the user.
    Returns:
    """
    previous_count = 1
    line_number = 0
    integer = 1
    output = ''
    while True:
        current_count = 1
        while True:
            if current_count == previous_count + 1:
                output = "{0}{1}".format(output, '\n')
                previous_count = current_count
                break
            output = "{0} {1}".format(output, integer)
            current_count += 1
            integer += 1
        line_number += 1
        if line_number == number:
            break
    print output


if __name__ == '__main__':
    print_traingle(get_user_input())
