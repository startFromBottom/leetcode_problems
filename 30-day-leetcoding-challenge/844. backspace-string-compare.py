"""

problem link : https://leetcode.com/problems/backspace-string-compare/
submission detail : https://leetcode.com/problems/backspace-string-compare/submissions


"""
from itertools import zip_longest


class Solution:
    """

    Time Complexity : O(n)

    """

    def backspaceCompare(self, S: str, T: str) -> bool:
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in zip_longest(F(S), F(T)))
