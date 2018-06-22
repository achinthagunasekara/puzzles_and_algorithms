""" Solution to `Minimum Sum Partition` puzzle """


INPUT = [
    [1, 6, 5, 11], # (1+5+6) - (11)
    [36, 7, 46, 40] # (46+7) - (36+40)
]


if __name__ == '__main__':
    for each_list in INPUT:
        each_list.sort()
        min_diff = None
        total_one = None
        total_two = None

        for index, each_from_start in enumerate(each_list):
            if index < len(each_list) - 1:
                if total_one:
                    total_one += each_from_start
                else:
                    total_one = each_list[-1] + each_from_start

                total_two = sum(each_list[index + 1:len(each_list) - 1])
                current_diff = abs(total_one - total_two)

                if not min_diff:
                    min_diff = current_diff
                else:
                    if min_diff > current_diff:
                        min_diff = current_diff
        print min_diff
