# https://leetcode.com/problems/rotate-image


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            new_row = []
            for row in range(length-1, -1, -1):
                new_row.append(matrix[row][i])
            matrix.append(new_row)
        matrix[:length] = []
