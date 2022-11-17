# https://leetcode.com/problems/n-th-tribonacci-number

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            t0, t1, t2 = 0, 1, 1
            while (n-2 > 0):
                t_new = t0+t1+t2
                t0, t1, t2 = t1, t2, t_new
                n -= 1
            return t_new
