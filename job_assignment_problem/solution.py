''' Solution to job assignment problem '''

import sys
import logging


def slice_list(list_in, sub_list_len=2):
    """
    Slice given list into sub lists.
    Args:
        list_in (list): List to slice into sub lists.
        sub_list_len (int): Length of each sub list.
    Returns:
        list: List containing sub lists.
    """
    list_of_lists = []
    start = 0
    for index in xrange(sub_list_len):
        stop = start + len(list_in[index::sub_list_len])
        list_of_lists.append(list_in[start:stop])
        start = stop
    return list_of_lists


def get_input():
    '''
    Get input from the user.
    Args:
    Returns:
        list: List of test cases to run.
    '''
    get_input_logger = logging.getLogger('get_input')
    input_test_cases = []
    try:
        num_test_cases = int(raw_input('Enter the number of test cases: '))
        for _ in xrange(num_test_cases):
            number_of_people = int(raw_input('Enter the number of people: '))
            efficiency = raw_input('Enter the efficiency for each person for each job: ')
            efficiency_list = map(int, efficiency.split(' '))
            if len(efficiency_list) != number_of_people ** 2:
                get_input_logger.error("Bad input for efficiency. There must be %s "
                                       "elements in the input",
                                       number_of_people ** 2)
                return None
            input_test_cases.append(
                slice_list(list_in=efficiency_list, sub_list_len=number_of_people)
            )
        return input_test_cases
    except ValueError as val_ex:
        logger.error("Something went wrong getting input from user - %s", val_ex)


def get_min_time_to_complete(test_case, loop=0, total_time=0):
    """
    Get the minimum time to complete a given test case.
    Args:
        list: List time for each person to complete each job.
    Returns:
        int: Total time to complete the job list.
    """
    # Since num of people == num of jobs
    while loop <= len(test_case[0]):
        min_time_for_job = None
        for each_person in test_case:
            min_time_for_person_for_job = each_person[0]
            if min_time_for_job is None or min_time_for_job > min_time_for_person_for_job:
                min_time_for_job = min_time_for_person_for_job
            each_person.pop(0)
        loop += 1
        total_time += min_time_for_job
        total_time = get_min_time_to_complete(test_case=test_case, loop=loop, total_time=total_time)
    return total_time


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('solution')  # pylint: disable=invalid-name
    test_cases = get_input()  # pylint: disable=invalid-name
    if not test_cases:
        sys.exit(1)
    for test_case_num, each_test_case in enumerate(test_cases):
        logger.info("Minimum time to do the job for test case %s is: %s",
                    test_case_num, get_min_time_to_complete(test_case=each_test_case))
