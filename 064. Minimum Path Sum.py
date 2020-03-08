"""

problem link : https://leetcode.com/problems/minimum-path-sum/
submission detail : https://leetcode.com/submissions/detail/310496418/

"""
from typing import List


class Solution:
    """

    Time Complexity : O(M * N)

    M * N matrix

    """

    def minPathSum(self, grid: List[List[int]]) -> int:

        N = len(grid)
        M = len(grid[0])

        if M == 0:
            return None

        min_path_sums = [[0 for _ in range(M)] for _ in range(N)]
        min_path_sums[0][0] = grid[0][0]

        for i in range(1, M):
            min_path_sums[0][i] = min_path_sums[0][i - 1] + grid[0][i]

        for j in range(1, N):
            min_path_sums[j][0] = min_path_sums[j - 1][0] + grid[j][0]

        print(min_path_sums)

        for i in range(1, N):
            for j in range(1, M):
                min_path_sums[i][j] = (
                    min(min_path_sums[i - 1][j], min_path_sums[i][j - 1]) + grid[i][j]
                )

        return min_path_sums[-1][-1]
