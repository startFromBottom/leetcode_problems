"""

problem link : https://leetcode.com/problems/jump-game/

"""
from typing import List


class Solution1:
    """

    Time Complexity : O(n)
    Space Complexity: O(1)

    discussion link : https://leetcode.com/problems/jump-game/discuss/538711/Intuitive-Solution-No-DP-Needed-(Explanations-included)

    """

    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        best = 0  # What is the furthest index we can reach so far?
        for i, v in enumerate(nums[:-1]):
            if best >= i:
                best = max(best, i + v)
            if best >= len(nums) - 1:  # If best is at or passed target, we're done
                return True
        return len(nums) == 1
