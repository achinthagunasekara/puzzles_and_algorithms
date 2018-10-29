"""
Adding a solution to balancing scale puzzle.
"""


def scale_balancing(int_list):
    """
    Get what weights needs to be added to balance the scale.
    Args:
        int_list (list): List of integers with what's on the scale and available weights.
    Returns:
        list: List of weights that must be added to each side.
    """
    on_scale = int_list[0]
    weights = int_list[1]

    for out_index, out_each_weight in enumerate(weights):
        for in_index, in_each_weight in enumerate(weights):
            if out_index != in_index:
                if on_scale[0] + out_each_weight == on_scale[1] + in_each_weight:
                    return (out_each_weight, in_each_weight)
    return None


TEST_CASES = [
    [
        [5, 9],
        [1, 2, 6, 7]
    ]
]


if __name__ == '__main__':
    for test_case in TEST_CASES:
        print("{0} => {1}".format(test_case, scale_balancing(int_list=test_case)))
