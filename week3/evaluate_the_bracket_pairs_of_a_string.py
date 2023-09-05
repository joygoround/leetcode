#  https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        list_to_dict = {key: value for key, value in knowledge}
        key_output_list = ["", ""]
        cursor = 1
        for char in s:
            if char == "(":
                cursor = 0
            elif char == ")":
                if key_output_list[0] in list_to_dict:
                    key_output_list[1] += list_to_dict[key_output_list[0]]
                else:
                    key_output_list[1] += "?"
                key_output_list[0] = ""
                cursor = 1
            else:
                key_output_list[cursor] += char
        return key_output_list[1]
