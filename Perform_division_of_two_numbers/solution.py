"""
Solution - Perform division of two numbers without using division operator (/).
"""

def devide_one(first, second):
    """
    Devide 2 numbers without using (/) operator.
    Args:
        first (int): First integer.
        second (int): Second integer.
    Returns:
         None
    """
    if second == 0:
        raise ZeroDivisionError("Unable to devide by zero ({0}/{1})".format(first, second))

    sign = bool((first * second) >= 0)
    first = abs(first)
    second = abs(second)
    quotient = 0

if __name__ == '__main__':
    pass
