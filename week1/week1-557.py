
# https: // leetcode.com/problems/reverse-words-in -a-string-iii/
# 557. Reverse Words in a String III

# took about 20min but had to look up some built in functions which I forgot

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splited = s.split()
        answer = ""
        for word in splited:
            rev = "".join(reversed(word))
            answer += (rev+" ")
        return answer[:-1]
