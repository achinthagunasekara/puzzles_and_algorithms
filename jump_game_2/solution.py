""" My Solution to Jump Game II """

class Solution1(object):
    """ First solution """

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(num_list=nums, stop_at_index=(len(nums) - 1))

    def helper(self, num_list, stop_at_index, max_jumps=0):
        """ Helper function for getting number of jumps """
        for index, value in enumerate(num_list):
            if index < stop_at_index:
                if value >= (stop_at_index - index):
                    max_jumps += 1
                    stop_at_index = index
                    return self.helper(num_list=num_list,
                                       stop_at_index=stop_at_index,
                                       max_jumps=max_jumps)
            else:
                return max_jumps


class Solution2(object):
    """ Second solution """

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_jumps = 0
        stop_at = len(nums) - 1
        while stop_at > 0:
            num_jumps, stop_at = self.helper(nums=nums,
                                             num_jumps=num_jumps,
                                             stop_at=stop_at)
        return num_jumps

    def helper(self, nums, num_jumps, stop_at):  # pylint: disable=no-self-use
        """
        Helper function to get number of jumps to a give index
        :type nums: List[int]
        :type num_jumps: int
        :type stop_at: int
        """
        for index in range(stop_at):
            if nums[index] >= stop_at:
                num_jumps += 1
                stop_at = index
                return num_jumps, stop_at
            stop_at -= 1


class Solution3(object):  # pylint: disable=too-few-public-methods
    """ Third solution """

    def jump(self, nums):  # pylint: disable=no-self-use
        """
        :type nums: List[int]
        :rtype: int
        """
        num_jumps = last_index = next_index = 0
        while next_index < len(nums) - 1:
            num_jumps += 1
            last_index, next_index = next_index, max(i + nums[i] for i in xrange(last_index, next_index + 1))  # pylint: disable=line-too-long
        return num_jumps


test_cases = [  # pylint: disable=invalid-name
    [2, 3, 1, 1, 4],
    [12, 3, 1, 1, 4],
    [1, 3, 1, 1, 4],
    [1, 1, 1, 1, 4],
    [1, 1, 1, 9, 4],
    [3, 1, 1, 1, 4]
]

print "Using first solution"

for test_case in test_cases:
    solution1 = Solution1()
    jumps = solution1.jump(test_case)
    print "%s --> %s" % (test_case, jumps)

print "Using second solution"

for test_case in test_cases:
    solution2 = Solution2()
    jumps = solution2.jump(test_case)
    print "%s --> %s" % (test_case, jumps)

print "Using third solution"

for test_case in test_cases:
    solution3 = Solution3()
    jumps = solution3.jump(test_case)
    print "%s --> %s" % (test_case, jumps)
