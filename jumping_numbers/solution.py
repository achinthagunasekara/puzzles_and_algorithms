#!/usr/local/bin/python

"""
Find jumping numbers.
"""


def get_jumping_numbers(orgianl_number, input_int, results):
    """
    Get all possible jumping numbers for a given integer.
    Args:
        orgianl_number (int): Orginal input numbers to search for jumping numbers in.
        input_int (int): Current int to search jumping numbers for.
        results (list): List to append any jumping numbers found.
    Returns:
        results (list): List of found jumping numbers.
    """
    if input_int <= orgianl_number:
        num_list = map(int, str(input_int))
        minus_list = list(num_list)
        plus_list = list(num_list)

        if len(num_list) == 1:
            results.append(num_list[0])

        minus = plus_list[len(plus_list) - 1] - 1
        if minus >= 0:
            minus_list.append(minus)
            new_int = reduce(lambda x, y: str(x)+str(y), minus_list)
            if int(new_int) <= orgianl_number:
                results.append(new_int)
            get_jumping_numbers(orgianl_number=orgianl_number, input_int=new_int, results=results)

        plus = plus_list[len(plus_list) - 1] + 1
        plus = plus if plus < 10 else 1
        plus_list.append(plus)
        new_int = reduce(lambda x, y: str(x)+str(y), plus_list)
        if int(new_int) <= orgianl_number:
            if not new_int.startswith("0"):
                results.append(new_int)
        get_jumping_numbers(orgianl_number=orgianl_number, input_int=new_int, results=results)
    return results

def get_jumping_nums_for_a_number(number):
    """
    Get all jumping numbers for a number.
    Args:
        number (int): Integer to check jumping numbers for.
    Returns:
        list: List of jumping numbers for the given integer.
    """
    output = []
    for each_int in range(number + 1):
        get_jumping_numbers(orgianl_number=number, input_int=each_int, results=output)
    return output


if __name__ == '__main__':
    INPUT_INTS = [
        10,
        35,
        50,
        54
    ]
    for integer in INPUT_INTS:
        print "%s ==> %s" % (integer, get_jumping_nums_for_a_number(number=integer))
