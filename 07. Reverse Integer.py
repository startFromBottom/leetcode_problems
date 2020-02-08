"""
problem link : https://leetcode.com/problems/reverse-integer/
submission detail : https://leetcode.com/submissions/detail/301065977/

"""


class Solution:
    def reverse(self, x: int) -> int:

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        rev = 0
        positive = 1
        if x < 0:
            positive = -1

        x = x * positive

        while x != 0:
            pop = x % 10
            x = x // 10
            if rev > INT_MAX / 10:
                return 0
            if rev < INT_MIN / 10 or (rev == INT_MIN / 10 and pop < -8):
                return 0
            rev = rev * 10 + pop

        return rev * positive
