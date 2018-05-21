""" Script for sorting elements of an list by frequency """


def append_to_sorted_list(unique, count, output):
    """
    Go through the list and append to sorted list.
    Args:
        unique (list): Unique items in the orginal list.
        count (list): Count of each unique items in the each list.
        output (list): Sorted list.
    Returns:
        list: Sorted list.
    """
    if len(count) <= 0:
        return output
    largest = None
    largest_index = None
    for index, each in enumerate(count):
        if each > largest:
            largest = each
            largest_index = index
    for _ in range(largest):
        output.append(unique[largest_index])
    del unique[largest_index]
    del count[largest_index]
    output = append_to_sorted_list(unique=unique, count=count, output=output)
    return output


def sort_list_by_frequency(input_list):
    """
    Sort a given list by frequency of items.
    Args:
        input_list (list): Input list for sorting.
    Returns:
        list: Sorted list.
    """
    output = []
    count = []
    unique = list(set(input_list))
    for each_unique in unique:
        count.append(input_list.count(each_unique))
    return append_to_sorted_list(unique=unique, count=count, output=output)


INPUT = [
    [5, 5, 4, 6, 4],
    [5, 6, 7, 7, 7, 5, 5, 1, 2, 1, 5, 1, 1, 1, 1]
]

if __name__ == '__main__':
    for each_input in INPUT:
        print sort_list_by_frequency(input_list=each_input)
