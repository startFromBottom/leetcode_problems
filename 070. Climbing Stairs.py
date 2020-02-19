"""

problem link : https://leetcode.com/problems/climbing-stairs/
submission detail : https://leetcode.com/submissions/detail/304841336/

"""


class Solution:
    """

    Time Complexity : O(n)

    """
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        b = [1, 2]
        for i in range(n - 2):
            b.append(b[-1] + b[-2])
        return b[-1]
