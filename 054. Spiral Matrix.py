from typing import List

"""

problem link : https://leetcode.com/problems/spiral-matrix/
submission detail : https://leetcode.com/submissions/detail/306405193/

"""


class Solution:
    """

     Time Complexity : O(?) : difficult ...
     m : num of rows
     n : num of columns

    """

    def spiral_outside(self, matrix: List[List[int]]) -> List[int]:

        arr = []
        num_row = len(matrix)
        num_col = len(matrix[0])
        if num_row == 1:
            return matrix[0]
        # add outside values in clockwise direction
        if num_col == 1:
            for row in matrix:
                arr.extend(row)
            return arr

        arr.extend(matrix[0])
        for r in range(1, num_row):
            arr.append(matrix[r][-1])
        arr.extend(list(reversed(matrix[-1][:-1])))
        for r in range(num_row - 2, 0, -1):
            arr.append(matrix[r][0])

        return arr

    def delete_outside(self, matrix: List[List[int]]) -> List[int]:

        # delete outside rows
        matrix = matrix[1:-1]
        # delete outsdie rows
        for i, v in enumerate(matrix):
            matrix[i] = matrix[i][1:-1]
        return matrix

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []

        while matrix and len(matrix[0]) > 0:
            ans.extend(self.spiral_outside(matrix))
            matrix = self.delete_outside(matrix)

        return ans
