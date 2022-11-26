# https://leetcode.com/problems/reduce-array-size-to-the-half/description/


from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        sorted_cout = sorted(list(Counter(arr).values()))

        output = 0
        sum = 0

        while (sum < len(arr)/2):
            sum += sorted_cout[-output-1]
            output += 1
        return output


# use Counter to create dict with element : counts, get only values and sort them
# set sum to 0, loop until it is over half of the length of arr
# add up from the largest value of counts and check
