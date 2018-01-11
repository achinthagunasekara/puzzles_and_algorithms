""" Solution """

# pylint: disable=invalid-name

people_list = [
    ["John", "john@gmail.com", "john@linkedin.com"],
    ["Dan", "dan@gmail.com", "+1234567"],
    ["john123", "+5412312", "john123@skype.com"],
    ["john1985", "+5412312", "john@linkedin.com"]
]

all_unique = []

def find_unique(unique, index, people):
    """ Find unique for a given index """
    for loop_index, person in enumerate(people):
        if len(set(people[index] + person)) < 6:
            if not loop_index in unique:
                unique.append(loop_index)
                if index != loop_index:
                    unique = find_unique(unique, loop_index, people)
    return unique

for current_index, each_person in enumerate(people_list):
    if not any(current_index in index for index in all_unique):
        all_unique.append(find_unique([], current_index, people_list))

print all_unique
