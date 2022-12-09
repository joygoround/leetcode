# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(list(word)))
            result[sorted_word] += [word]
        return result.values()
