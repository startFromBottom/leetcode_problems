"""

problem link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
submission detail : https://leetcode.com/submissions/detail/303470779/

"""

from typing import List


class Solution:
    """

    Time Complexity : O(n)

    """
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i - 1] == nums[i]:
                del nums[i - 1]
            else:
                i += 1
        return len(nums)
