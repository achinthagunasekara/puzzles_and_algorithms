""" Find the closest palindrome number to a given number """


def find_closest_palindrome(number):
    """
    Find the closest palindrome number to a given number.
    Args:
        number (int): Input number.
    Returns:
        int: Closest palindrome number to the given number.
    """
    new_list = None
    number_list = map(int, str(number))

    if len(number_list) == 1:
        return number_list[0] - 1

    sliced_num_list = number_list[:len(number_list)/2]
    if len(number_list) % 2 == 0:
        new_list = sliced_num_list + \
                sliced_num_list[::-1]
    else:
        new_list = sliced_num_list + \
                   [number_list[len(number_list)/2]] + \
                   sliced_num_list[::-1]
    return int(reduce(lambda x, y: "%s%s" % (x, y), new_list))


if __name__ == '__main__':
    INPUT = [
        9,
        489,
        2212,
        23224
    ]
    for each_input in INPUT:
        print "%s => %s" % (each_input, find_closest_palindrome(number=each_input))
