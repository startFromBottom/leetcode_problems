"""

problem link : https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/
submission detail : https://leetcode.com/submissions/detail/314821192/


"""

from collections import deque
from typing import List

class Solution:
    """

    use BFS algorithm
    Time Complexity : O(M * N)
    M : height of grid
    N : width of grid

    """

    def hasValidPath(self, grid: List[List[int]]) -> bool:

        M, N = len(grid[0]), len(grid)

        left = (0, -1)
        right = (0, 1)
        up = (-1, 0)
        down = (1, 0)

        # 각 street에서 이동 가능한 방향
        move_directions = {
            1: (left, right),
            2: (up, down),
            3: (left, down),
            4: (right, down),
            5: (left, up),
            6: (right, up)
        }

        # 다음 타일의 방향과 매칭
        # 예) 현재 타일이 아래 방향이면, 다음 타일에는 윗 방향이 있어야 한다.
        matching = {left: right, right: left, up: down, down: up}

        q = deque([(0,0)])
        visited = set()
        visited.add((0, 0))

        while q:
            m, n = q.popleft()
            if (m, n) == (N - 1, M - 1):
                return True
            directions = move_directions[grid[m][n]]
            for d in directions:
                x, y = d
                if 0 <= m + x <= N - 1 and 0 <= n + y <= M - 1 and (m + x, n + y) not in visited:
                    # check compatibility
                    next_street = grid[m + x][n + y]
                    if matching[d] in move_directions[next_street]:
                        visited.add((m + x, n + y))
                        q.append((m + x, n + y))

        return False