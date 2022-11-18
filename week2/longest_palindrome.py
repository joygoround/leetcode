# https://leetcode.com/problems/longest-palindrome/description/


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 1:
            return 1

        result = 0
        bag_of_char = set()

        for char in s:
            if char in bag_of_char:
                result += 2
                bag_of_char.remove(char)
            else:
                bag_of_char.update(char)

        return result if len(bag_of_char) == 0 else result+1
