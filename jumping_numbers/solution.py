"""
Find jumping numbers.
"""


def get_jumping_numbers(orgianl_number, input_int, results):
    """ Get jumping numbers """

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


if __name__ == '__main__':
    INPUT = [
        35
    ]
    output = []
    for integer in INPUT:
        for each_int in range(integer + 1):
            get_jumping_numbers(orgianl_number=integer, input_int=each_int, results=output)
    print output
