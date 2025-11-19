class solver:
    def __init__(self):
        return None

    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and
        you may not use the same element twice.

        You can return the answer in any order.
        """

        dict_of_nums = {}
        for i in range(len(nums)):
            dict_of_nums[nums[i]] = i
            # make new entry with num as the key
            # and its index as the value

        for i in range(len(nums)):
            if target - nums[i] in dict_of_nums:
                if dict_of_nums[target - nums[i]] != i:
                    return [i,dict_of_nums[target - nums[i]]]
            # first if statement queries existence of desired summand
            # second if statement makes sure same element isn't used twice
        return [0,0]
