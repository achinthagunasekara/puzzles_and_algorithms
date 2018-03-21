"""
Find jumping numbers.
"""

def build_list(number):
    """
    Get jumping numbers between 0 and given integer.
    Args:
        integer (int): Integer to check up to.
    Return:
        String: String of all jumping numbers.
    """
    int_list = list(str(number))
    return int_list


def get_jumping_numbers(number, current_digit=0, index=0):
    jumping_numbers = []
    integer_list = build_list(number=number)
    while index < len(integer_list):
        for each_int in range(10):
            if current_digit - 1 == each_int or current_digit + 1 == each_int:
                try:
                    jumping_numbers.append(int("%s%s" % (jumping_numbers[-1], each_int)))
                except IndexError:
                    jumping_numbers.append(each_int)
                index += 1
                jumping_numbers = jumping_numbers + get_jumping_numbers(number=number, current_digit=each_int, index=index)
    return jumping_numbers


INPUT = [
    10
]

for integer in INPUT:
    print get_jumping_numbers(number=integer)
    print '======'
