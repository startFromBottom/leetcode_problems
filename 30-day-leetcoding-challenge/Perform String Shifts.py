"""

problem link : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

"""
from typing import List


class Solution:
    """

    Time Complexity : O (n)

    """
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        def move_left(s, a: int):
            for _ in range(a):
                s = s[1:] + s[0]
            return s

        def move_right(s, a: int):
            for _ in range(a):
                s = s[-1] + s[:-1]
            return s

        for m in shift:
            d, a = m
            if d == 0:  # move left
                s = move_left(s, a)
            else:  # move right
                s = move_right(s, a)

        return s
