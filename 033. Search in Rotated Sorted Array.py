"""

problem link : https://leetcode.com/problems/search-in-rotated-sorted-array/
submission detail : https://leetcode.com/submissions/detail/306742115/

"""
from typing import List


class Solution:
    """
    Time Complexity: O(logn)

    """

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        if target == nums[l]:
            return l
        return -1
