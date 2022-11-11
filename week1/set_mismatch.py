# https://leetcode.com/problems/set-mismatch/

# took longer time due to not considering unordered parameter


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        check = {i+1: 0 for i in range(len(nums))}
        doubled = 0

        for num in nums:
            if check[num] == 0:
                check[num] += 1
            else:  # already there
                doubled = num

        for key in check.keys():
            if check[key] == 0:
                return [doubled, key]
