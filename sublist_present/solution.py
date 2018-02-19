"""
Check if a given list contains a second given list
"""


def check_sub_arr(current_index, list1, list2):
    """
    Check if given part of the first list contain the second list.
    Args:
        current_index (int): Index on the first list to start checking from.
        list1 (list): List to search in.
        list2 (list): List to be found.
    Returns:
        bool: True if found, False otherwise.
    """
    for index_2, num in enumerate(list2):
        try:
            if num != list1[current_index + index_2]:
                return False
        except IndexError:
            return False
    return True


def check_list(list1, list2):
    """
    Check if given first list contain the second list.
    Args:
        list1 (list): List to search in.
        list2 (list): List to be found.
    Returns:
        int: If found, index of the start, if not -1.
    """
    index = len(list1) - 1
    output = -1

    while index >= 0:
        if check_sub_arr(index, list1, list2):
            output = index
            break
        index -= 1
    return output


input_1 = [1, 2, 3, 1, 2, 3]  # pylint: disable=invalid-name
input_2 = [2, 3]  # pylint: disable=invalid-name
print check_list(input_1, input_2)
