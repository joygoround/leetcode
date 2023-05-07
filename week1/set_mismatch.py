# https://leetcode.com/problems/set-mismatch/


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


"""  ------- review ----------
Intuitive way : compareing one to one
O(n) complecity but multiple times of for loop
"""

"""  Solution 2
"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        summation = int((len(nums) + 1) * len(nums) / 2)
        actual_sum = 0
        exists = set()
        doubled = 0

        for num in nums:
            if num in exists:
                double = num
            else:
                exists.add(num)
            actual_sum += num
        return [doubled, summation - actual_sum + double]


"""  ------- review ----------
Using summation of numbers to compare the duplicates.
"""
