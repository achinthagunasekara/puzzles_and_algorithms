"""
Find jumping numbers.
"""


def get_jumping_numbers(orgianl_number, input_int, position=0):
    """ Get jumping numbers """
    num_list = map(int, str(input_int))
    if len(num_list) > position and num_list[position] > 0:
        try:
            jumping_number_less = int("%s%s" % (num_list[position], (num_list[position] - 1)))
            print "POS %s POS - 1 %s and %s" % (num_list[position], (num_list[position] - 1), jumping_number_less)
            if jumping_number_less >= 0 and jumping_number_less <= orgianl_number:
                print "LESS %s" % jumping_number_less
        except ValueError:
            # do nothing
            pass
        jumping_number_more = int("%s%s" % (num_list[position], (num_list[position] + 1)))
        if jumping_number_more >= 0 and jumping_number_more <= orgianl_number:
            print "more %s" % jumping_number_more
        position += 1
        get_jumping_numbers(orgianl_number=orgianl_number, input_int=input_int, position=position)


def check_each_num(input_int):
    """ Get jumping numbers """
    for each_int in range(input_int + 1):
        position = 0
        if each_int < 10:
            print "input %s" % each_int
            print "++++++++++++"
        get_jumping_numbers(orgianl_number=input_int, input_int=each_int, position=position)


if __name__ == '__main__':
    INPUT = [
        12
    ]
    for integer in INPUT:
        print check_each_num(input_int=integer)
        print '======'
