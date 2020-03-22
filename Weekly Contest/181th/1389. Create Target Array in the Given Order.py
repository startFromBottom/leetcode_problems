"""

problem link : https://leetcode.com/problems/create-target-array-in-the-given-order/
submission detail : https://leetcode.com/contest/weekly-contest-181/submissions/detail/314666635/


"""
from typing import List


class Solution:
    """

    Time Complexity

    best case : O(n)
    worst case : O(n^2)

    """
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i, value in enumerate(index):
            target.insert(value, nums[i])
        return target

