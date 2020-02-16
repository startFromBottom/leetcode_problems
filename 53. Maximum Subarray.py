"""

problem link : https://leetcode.com/problems/maximum-subarray/
submission detail : https://leetcode.com/submissions/detail/303831151/

"""

from typing import List

class Solution:
    """
    Time Complexity : O(n)

    """
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = nums[i] if cur_sum < 0 else cur_sum + nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum