""" Solution to simple fraction puzzle """

def get_floating_points(number, divide_by):

    """
    Divide a number by a given number.
    Args:
        number (int): Number to divide.
        divide_by (int): Number to divide by.
    Returns:
        str: Result of the division.
    """
    return number / float(divide_by)

def divide(number, divide_by):
    """
    Divide a number by a given number.
    Args:
        number (int): Number to divide.
        divide_by (int): Number to divide by.
    Returns:
        str: Result of the division.
    """
    division = number / divide_by
    remainder = number % divide_by
    if not remainder:
        return division
    return get_floating_points(number=remainder, divide_by=divide_by)

NUMBERS = [
    (4, 2),
    (8, 3)
]

if __name__ == '__main__':
    for each_num in NUMBERS:
        print divide(number=each_num[0], divide_by=each_num[1])
