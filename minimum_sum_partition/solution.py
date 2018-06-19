""" Solution to `Minimum Sum Partition` puzzle """


INPUT = [
    [1, 6, 5, 11],
    [36, 7, 46, 40]
]


if __name__ == '__main__':
    for each_list in INPUT:

        #print "Processing list %s" % each_list
        each_list.sort()
        print "Processing list %s" % each_list

        first_sub_list_total = 0
        min_difference = None
        min_split_index = None

        for outter_index, each_element in enumerate(each_list):
            second_sub_list_total = 0
            first_sub_list_total += each_element


            for inner_index in range(outter_index + 1, len(each_list)):
                second_sub_list_total += each_list[inner_index]

            current_difference = abs(first_sub_list_total - second_sub_list_total)
            print current_difference

            if not min_difference:
                min_difference = current_difference
                min_split_index = outter_index + 1

            if current_difference < min_difference:
                min_difference = current_difference
                min_split_index = outter_index + 1

        print "List can be split as %s and %s" % (each_list[:min_split_index],
                                                  each_list[min_split_index:])
        print "Difference between two lists is %s" % min_difference
        print "=================================="
