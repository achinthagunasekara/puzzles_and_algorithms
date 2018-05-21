""" Find the largest subarray of 0's and 1's """


def check_list(input_list):
    """
    Check if a list has equal number of 0s and 1s.
    Args:
        input_list (list): List to check if it has equal number of 0s and 1s.
    Returns:
        int: Number of 0s or 1s in the list. None if number of 0s and 1s are not equal.
    """
    if input_list.count(0) == input_list.count(1):
        return input_list.count(0)
    return None

def get_logest_0s_and_1s_sub_list(input_list):
    """
    Get the longest sub list with equal number of 0s and 1s.
    Args:
        input_list (list): Return the start and end indexes of longest sub list(s),
                           with equal number of 0s and 1s.
    Returns:
        list: List of tuples with start and end indexes of sub lists.
    """
    previous_count = 0
    indexes = []
    for first_index in range(len(input_list)):
        for second_index in range(first_index, len(input_list)):
            if first_index < second_index:
                sub_list = input_list[first_index:second_index + 1]
                count_items = check_list(input_list=sub_list)
                if count_items > previous_count:
                    previous_count = count_items
                    indexes = []
                    indexes.append((first_index, second_index))
                elif count_items == previous_count:
                    indexes.append((first_index, second_index))
    return indexes

if __name__ == '__main__':
    INPUT = [
        [1, 0, 1, 1, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 1, 0]
    ]
    for each_input in INPUT:
        print get_logest_0s_and_1s_sub_list(input_list=each_input)
