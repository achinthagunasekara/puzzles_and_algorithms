"""
Solution to Count the triplests with sum smaller than a given value.
"""


def count_triplets(list_in, less_than):
    """
    Count triplets with sum smaller than a given value.
    Args:
        list_in (list): List to search triplets in.
        less_than (int): Total less than this int.
    Returns:
        int: Number of triplets with sum smaller than a given value.
    """
    count = 0
    for one_index, one_each in enumerate(list_in):
        second_list = list_in[one_index + 1:]
        for two_index, two_each in enumerate(second_list):
            third_list = second_list[two_index + 1:]
            for _, three_each in enumerate(third_list):
                if (one_each + two_each + three_each) < less_than:
                    count += 1
    return count


TEST_CASES = [
    ([-2, 0, 1, 3], 2),
    ([5, 1, 3, 4, 7], 12)
]


if __name__ == '__main__':
    for each_test in TEST_CASES:
        print count_triplets(list_in=each_test[0],
                             less_than=each_test[1])
