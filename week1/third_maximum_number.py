# https://leetcode.com/problems/third-maximum-number/
# 20 min

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = removeMax(nums)
        second = removeMax(first)
        return max(nums) if len(second) == 0 else max(second)


def removeMax(list):
    if len(list) == 0:
        return []
    maxnum = max(list)
    removed = []
    for ele in list:
        if ele != maxnum:
            removed.append(ele)
        else:
            pass
    return removed
