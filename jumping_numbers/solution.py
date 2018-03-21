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


def get_jumping_numbers(number, current_digit=-1, index=0):
    jumping_numbers = []
    integer_list = build_list(number=number)

#    while index < len(integer_list):
    while index < 3:
        for each_int in range(10):
            if current_digit - 1 == each_int or current_digit + 1 == each_int:
                try:
                    append = int("%s%s" % (jumping_numbers[-1], each_int))
                except IndexError:
                    append = each_int
                print "STUPID NUMBER %s" % append
                if append <= number:
                    jumping_numbers.append(append)
                else:
                    return jumping_numbers
                index += 1
                jumping_numbers = jumping_numbers + get_jumping_numbers(number=number, current_digit=each_int, index=index)
#    index += 1
    return jumping_numbers


INPUT = [
    10
]

for integer in INPUT:
    print get_jumping_numbers(number=integer)
    print '======'
