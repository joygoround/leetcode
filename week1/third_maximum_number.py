# https://leetcode.com/problems/third-maximum-number/
# 20 min

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = remove_max(nums)
        second = remove_max(first)
        return max(nums) if len(second) == 0 else max(second)


def remove_max(nums):
    if len(nums) == 0:
        return []
    max_num = max(nums)
    removed = []
    for ele in nums:
        if ele != max_num:
            removed.append(ele)
    return removed
 """
 no need to use else if statement is pass
 nit : follow function naming name_func
 """