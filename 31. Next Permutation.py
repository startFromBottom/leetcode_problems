"""

problem link : https://leetcode.com/problems/next-permutation/
submission detail : https://leetcode.com/problems/next-permutation/submissions/

"""

from typing import List


class Solution:
    """

    Time Complexity : O(n)

    """

    def reverse(self, nums: List[int], start: int) -> None:
        i = start
        j = len(nums) - 1
        while j > i:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        # step 1 : finding first decreasing element (i)
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            # step 2 : finding number(j) just larger than nums[i]
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # step 3 : swap nums[i], nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            # step 4 : reverse elements (start : i+1)
            self.reverse(nums, i + 1)
        else:
            self.reverse(nums, 0)
