
# https: // leetcode.com/problems/reverse-words-in -a-string-iii/
# 557. Reverse Words in a String III

# took not long time to solve but had to look up some built in functions which I forgot

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        fianl = ""
        for word in s.split():
            rev = "".join(reversed(word))
            fianl += (rev+" ")
        return fianl[:-1]


"""
reversed(word) == word[::-1]
keep the code simple, do not use extra variable when it's not needed

"""
