"""

problem link : https://leetcode.com/problems/remove-element/
submission detail : https://leetcode.com/submissions/detail/303469905/

"""
from typing import List


class Solution:
    """

    Time Complexity : O(n)

    """
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)
