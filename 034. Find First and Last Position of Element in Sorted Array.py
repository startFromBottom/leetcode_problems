"""

problem link : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
submission detail : https://leetcode.com/submissions/detail/307365292/

"""

from typing import List


class Solution:
    """

    Time Complexity: O(logn + logn) = O(logn)
    n : length of nums

    """

    def set_initial_value(self, nums: List[int]) -> List[int]:
        """
        set initival value of lo, hi, ans
        """
        return 0, len(nums) - 1, -1

    def upper_bound(self, nums: List[int], target: int) -> List[int]:
        """
        find last position of element
        """
        lo, hi, ans = self.set_initial_value(nums)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                ans = mid
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

    def lower_bound(self, nums: List[int], target: int) -> List[int]:
        """
        find first position of element
        """
        lo, hi, ans = self.set_initial_value(nums)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                ans = mid
                hi = mid - 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[List[int]]:
        return [self.lower_bound(nums, target), self.upper_bound(nums, target)]          
