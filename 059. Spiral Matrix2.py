"""

problem link : https://leetcode.com/problems/spiral-matrix-ii/
submission detail : https://leetcode.com/problems/spiral-matrix-ii/

"""
from typing import List


class Solution:
    """

    Time Complexity: O(n * n)
    
    n*n matrix

    """

    def generateMatrix(self, n: int) -> List[List[int]]:

        ans = [[0 for _ in range(n)] for _ in range(n)]

        # step 1 : 껍데기의 개수(?) 구하기
        shell_cnt = n // 2 if n % 2 == 0 else n // 2 + 1

        # step 2 : for문 한번 돌때마다 외곽 값들이 채워짐
        k = 1
        for idx in range(shell_cnt):
            # fill outside(clockwise direction)
            # top
            for i in range(idx, n - 1 - idx):
                ans[idx][i] = k
                k += 1
            # right
            for i in range(idx, n - 1 - idx):
                ans[i][(-1 - idx)] = k
                k += 1
            # bottom
            for i in range(n - 1 - idx, idx, -1):
                ans[(-1 - idx)][i] = k
                k += 1
            # left
            for i in range(n - 1 - idx, idx, -1):
                ans[i][idx] = k
                k += 1

        if n % 2 == 1:
            ans[n // 2][n // 2] = n ** 2

        return ans
