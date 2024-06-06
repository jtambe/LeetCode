# https://www.youtube.com/watch?v=ymOBPRt9UR0
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for row in range(n):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # print("Transpose")
        # print(matrix)

        for row in range(n):
            matrix[row].reverse()