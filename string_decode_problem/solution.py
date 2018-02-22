"""
If a=1, b=2, c=3 ... z=26. Given a string, find all possible codes that string,
can generate. Give a count as well as print the strings
"""


def get_a_to_z():
    """
    Set up a dictonery with A to Z values
    Args:
        None
    Returns:
        None
    """
    chars = {}
    key = 1
    for char in range(97, 123):
        chars[key] = chr(char)
        key += 1
    return chars


def get_sub_strings(input_string, current_index=0):
    """
    Take a input string of numbers and decode it to see what strings,
    it could represent.
    Args:
        input_string (String): String of integers.
    Returns:
        Dictionary: Dictionary of strings the input string could represent.
    """
    if current_index >= len(input_string):
        return
    tree = {}
    if current_index < (len(input_string) - 1):
        double_digits = int("%s%s" % (input_string[current_index], input_string[current_index + 1]))
        if double_digits <= 26:
            sub_tree = get_sub_strings(current_index=(current_index + 2), input_string=input_string)
            tree[double_digits] = sub_tree

    sub_tree = get_sub_strings(current_index=(current_index + 1), input_string=input_string)
    tree[int(input_string[current_index])] = sub_tree
    return tree



def print_data_structure(strucutre):
    """
    Print the data structure.
    Args:
        strucutre (dictionary): Dictionary of data.
    Returns:
        None
    """
    for key, data_items in strucutre.iteritems():
        print key
        if data_items:
            print_data_structure(data_items)


INPUT_STRINGS = [
    "1123",
]

for each_string in INPUT_STRINGS:
    data = get_sub_strings(input_string=each_string)
    print_data_structure(strucutre=data)

#print get_a_to_z()
