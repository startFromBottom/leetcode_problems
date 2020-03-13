"""

problem link : https://leetcode.com/problems/search-insert-position/
submission detail : https://leetcode.com/submissions/detail/312039356/

"""
from typing import List


class Solution:
    """

    Time Complexity: O(logn)

    """

    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while r >= l:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return l
