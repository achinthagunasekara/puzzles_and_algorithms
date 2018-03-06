"""
Given an array A of integers, find the maximum of j - i,
subjected to the constraint of A[i] <= A[j]
"""

def find_the_max_index(input_list):
    """
    Given an array A of integers, find the maximum of j - i.
    Args:
        list (list): List to search in.
    Returns:
        int: Maximum of j - i.
    """
    max_diff = None
    for outter_index, outter_value in enumerate(input_list):
        for inner_index in xrange(outter_index, len(input_list)):
            diff = input_list[inner_index] - outter_value
            if diff > max_diff:
                max_diff = diff
    return max_diff

if __name__ == "__main__":
    INPUTS = [
        [3, 5, 4, 2]
    ]
    for each_input in INPUTS:
        print "%s --> %s" % (each_input, find_the_max_index(each_input))
