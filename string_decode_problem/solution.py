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


LETTERS = get_a_to_z()


def generate_all_possible_combinations(input_string, current_index=0):  # pylint: disable=invalid-name
    """
    Take a input string of numbers and decode it to see what strings,
    it could represent.
    Args:
        input_string (String): String of integers.
    Returns:
        Dictionary: Dictionary of strings the input string could represent.
    """
    if current_index >= len(input_string):
        return None
    tree = {}
    if current_index < (len(input_string) - 1):
        double_digits = int("%s%s" % (input_string[current_index], input_string[current_index + 1]))
        if double_digits <= 26:
            sub_tree = generate_all_possible_combinations(current_index=(current_index + 2),
                                                          input_string=input_string)
            tree[double_digits] = sub_tree

    sub_tree = generate_all_possible_combinations(current_index=(current_index + 1),
                                                  input_string=input_string)
    tree[int(input_string[current_index])] = sub_tree
    return tree



def print_data_structure(strucutre, previous_structure=None):
    """
    Print the data structure.
    Args:
        strucutre (dictionary): Dictionary of data.
    Returns:
        None
    """
    for key, data_items in strucutre.iteritems():
        if previous_structure:
            current_structure = "%s%s" % (previous_structure, LETTERS[key])
        else:
            current_structure = LETTERS[key]
        if data_items is None:
            print current_structure
        else:
            print_data_structure(data_items, previous_structure=current_structure)


INPUT_STRINGS = [
    "1123",
]

for each_string in INPUT_STRINGS:
    data = generate_all_possible_combinations(input_string=each_string)
    print_data_structure(strucutre=data)
