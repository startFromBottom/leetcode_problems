"""

problem link : https://leetcode.com/problems/permutations/
submission detail : https://leetcode.com/submissions/detail/310508667/

"""
from typing import List


class Solution:
    """
    Time Complexity : O(n!)
    n : length of nums

    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        """
        ans = []

        def recursion(nums: List[int], arr: List[int]):
            if not nums:
                ans.append(arr)
                return
            for i in range(len(nums)):
                recursion(nums[:i] + nums[i+1:], arr + [nums[i]])

        recursion(nums, [])
        return ans