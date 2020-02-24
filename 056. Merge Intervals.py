"""

problem link : https://leetcode.com/problems/merge-intervals/
submission detail : https://leetcode.com/submissions/detail/306430166/

"""
from typing import List


class Solution:
    """

    Time Complexity : O(nlogn + n) = O(nlogn)
    n : length of intervals

    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        # step 1 : sort products ~ O(nlogn)
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        # step 2: overlapping intervals ~ O(n)
        overlap = [intervals[0]]
        for i in range(1, n):
            if overlap[-1][-1] >= intervals[i][0]:
                if overlap[-1][-1] >= intervals[i][-1]:
                    continue
                overlap[-1] = [overlap[-1][0], intervals[i][-1]]
            else:
                overlap.append(intervals[i])
        return overlap
