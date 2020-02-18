"""

problem link : https://leetcode.com/problems/rotate-image/
submission detail : https://leetcode.com/submissions/detail/304517097/

"""
from typing import List


class Solution:
    """
    Time Complexity : O( n(n-1)/2 + n^2/2) = O(n**2)
    n : length of matrix row
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # step 1 : swap element between rows
        # ex) swap matrix[0][1] and matrix[1][0], swap matrix[1][2] and matrix[2][1]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # step 2 : reverse each row
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
        return matrix
