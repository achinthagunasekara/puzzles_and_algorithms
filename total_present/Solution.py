""" Solution to finding total present puzzle """

class Solution(object):
    """ Solution class """

    # Following method will return the two numbers,
    # but not the indexes. But it'll be faster than looping though the lists.
    def two_sum_nums(self, nums, target):  # pylint: disable=no-self-use
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        needed = []
        for num in nums:
            if num in needed:
                return [num, (target - num)]
            else:
                needed.append(target - num)

    # For each element, we try to find its complement,
    # by looping through the rest of array which takes O(n) time.
    # Therefore, the time complexity is O(n2)
    def two_sum_indexes(self, nums, target):  # pylint: disable=no-self-use
        """
        Return the indexes of the elements
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num_one in enumerate(nums):
            for j, num_two in enumerate(nums):
                if num_one + num_two == target and i != j:
                    return [i, j]


test_cases = [  # pylint: disable=invalid-name
      [[4, 2, 3], 5],
      [[3, 2, 4], 6],
      [[2, 7, 11, 15], 9],
      [[2, 7, 11, 15], 12],
      [[2, 7, 11, 12], 23],
      [[2, 7, -26, 50], 24],
      [[2, 7, -11, 6], -5],
      [[2, 7, 5, 15], 7],
]

for test_case in test_cases:
    solution = Solution()
    print solution.two_sum_nums(test_case[0], test_case[1])
    print solution.two_sum_indexes(test_case[0], test_case[1])
