""" My Solution to Jump Game II """

def helper(num_list, stop_at_index, max_jumps=0):
    """ Helper function for getting number of jumps """
    for index, value in enumerate(num_list):
        if index < stop_at_index:
            if value >= (stop_at_index - index):
                max_jumps += 1
                stop_at_index = index
                return helper(num_list=num_list,
                              stop_at_index=stop_at_index,
                              max_jumps=max_jumps)
        else:
            return max_jumps

test_cases = [  # pylint: disable=invalid-name
    [2, 3, 1, 1, 4],
    [12, 3, 1, 1, 4],
    [1, 3, 1, 1, 4],
    [1, 1, 1, 1, 4],
    [1, 1, 1, 9, 4],
    [3, 1, 1, 1, 4]
]

for test_case in test_cases:
    jumps = helper(num_list=test_case,
                   stop_at_index=(len(test_case) - 1))
    print "%s --> %s" % (test_case, jumps)
