"""
problem link : https://leetcode.com/problems/3sum/
submission detail : https://leetcode.com/submissions/detail/301089824/

"""

from typing import List


class Solution:
    """
    O(n ** 2) Solution
    use twoSum solution to solve threeSum problem
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i, v in enumerate(nums):
            self.twoSum(nums[i + 1:], -v, ans)
        return ans

    def twoSum(self, nums, target, ans):
        d = {}
        for i, v in enumerate(nums):
            if target - v in d:
                ans.add((v, target - v, -target))  # 3sum wants the numbers, while 2sum wanted the indices
            d[v] = i
