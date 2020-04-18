from collections import deque
from typing import List


class Solution:
    """

    Time Complexity : O(w * h) - grid의 각 원소를 한 번만 접함
    BFS 사용

    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ans = 0
        w = len(grid[0])
        h = len(grid)
        visited = [[False for _ in range(w)] for _ in range(h)]
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1" and not visited[i][j]:
                    visited[i][j] = True
                    ans += 1
                    q = deque([(i, j)])
                    while q:
                        x, y = q.pop()
                        for m in moves:
                            n_x, n_y = x + m[0], y + m[1]
                            if 0 <= n_x < h and 0 <= n_y < w and grid[n_x][n_y] == "1" and not visited[n_x][n_y]:
                                visited[n_x][n_y] = True
                                q.appendleft((n_x, n_y))
        return ans
