"""

problem link : https://leetcode.com/problems/4sum/
submission detail : https://leetcode.com/submissions/detail/303466425/


"""
from typing import List, Set, Tuple


class Solution:
    """

    Time Complexity : O(n**3)

    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i, v in enumerate(nums):
            self.threeSum(nums[i + 1:], target - v, ans, v)
        return ans

    def threeSum(self, nums: List[int],
                 target: int,
                 ans: Set[Tuple[int, int, int, int]],
                 first: int) -> None:
        for i, v in enumerate(nums):
            self.twoSum(nums[i + 1:], target - v, ans, first, v)

    def twoSum(self, nums: List[int],
               target: int,
               ans: Set[Tuple[int, int, int, int]],
               first: int,
               second: int) -> None:
        d = {}  # key : each value of nums, value : index
        for i, v in enumerate(nums):
            if target - v in d:
                ans.add((first, second, v, target - v))
                d[v] = i
