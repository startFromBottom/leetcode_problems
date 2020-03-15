"""

problem link : https://leetcode.com/problems/lucky-numbers-in-a-matrix/
submission detail : https://leetcode.com/submissions/detail/312571476/

"""
from typing import List


class Solution:
    """

    Time Complexity : O(m * n)
    - m * n matrix

    """
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(matrix)):
            row_min = min(matrix[i])
            row_min_idx = matrix[i].index(row_min)
            col_max = row_min

            for j in range(len(matrix)):
                if matrix[j][row_min_idx] > col_max:
                    col_max = matrix[j][row_min_idx]

            if col_max == row_min:
                ans.append(col_max)

        return ans
