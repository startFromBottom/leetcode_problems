"""

problem link : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
submission detail : https://leetcode.com/submissions/detail/312275591/

"""
from typing import List


class Solution:
    """

    Time Complexity :
    Worst Case : O(n**2) (when remove element almost every iteration)
    Best Case : O(n) (when not remove element)

    """
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        same_cnt = 1
        val = nums[0]
        i = 1

        while i < len(nums):
            if same_cnt == 2 and nums[i] == val:
                del nums[i]
            elif nums[i] == val:
                same_cnt += 1
                i += 1
            else:  # nums[i+1] != nums[i]
                same_cnt = 1
                val = nums[i]
                i += 1

        return len(nums)
