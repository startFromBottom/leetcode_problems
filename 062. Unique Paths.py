"""

problem link : https://leetcode.com/problems/unique-paths/
submission detail : https://leetcode.com/submissions/detail/308581662/

"""
from collections import deque


class Solution:
    """
    Time Complexity : O(m * n)
    """

    def factorial(self, num: int):
        if num == 0 or num == 1:
            return 1
        return num * self.factorial(num - 1)

    def uniquePaths(self, m: int, n: int) -> int:
        return self.factorial(m + n - 2) // (self.factorial(m - 1) * self.factorial(n - 1))


class BadSolution:
    """
    use BFS

    Memory Limit Exceeded

    """

    def uniquePaths(self, m: int, n: int):
        q = deque()
        q.appendleft((1, 1))
        cnt = 0
        while q:
            point = q.pop()
            if point == (m, n):
                cnt += 1
                continue
            next_path1 = (point[0] + 1, point[1])
            if next_path1[0] <= m:
                q.appendleft(next_path1)
            next_path2 = (point[0], point[1] + 1)
            if next_path1[1] <= n:
                q.appendleft(next_path2)
        return cnt
