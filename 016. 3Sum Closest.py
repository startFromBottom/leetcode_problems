"""

problem link : https://leetcode.com/problems/3sum-closest/
submission detail : https://leetcode.com/problems/3sum-closest/submissions/

"""

from typing import List


class Solution:
    """
    O (n ** 2) Solution

    use two pointer

    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = 2147483647  # maximum value of integer
        n = len(nums)
        nums.sort()
        ans = 0

        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while r > l:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum == target:
                    return target
                if abs(three_sum - target) <= res:
                    res = abs(three_sum - target)
                    ans = three_sum
                if three_sum > target:
                    r -= 1
                else:
                    l += 1

        return ans