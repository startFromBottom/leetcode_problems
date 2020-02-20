"""

problem link : https://leetcode.com/problems/sort-colors/
submission detail : https://leetcode.com/submissions/detail/305157005/

"""


class Solution:
    """

    Time Complexity : O(n)
    constant space, one-pass algorithms
    (by using two pointers)

    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        p_l = 0
        p_r = len(nums) - 1
        while cur <= p_r:
            if nums[cur] == 0:
                nums[p_l], nums[cur] = nums[cur], nums[p_l]
                p_l += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[p_r], nums[cur] = nums[cur], nums[p_r]
                p_r -= 1
        return nums
