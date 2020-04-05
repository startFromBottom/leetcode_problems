"""

problem link : https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/
submission detail : https://leetcode.com/problems/move-zeroes/

"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Two-Pointer method

        Time Complexity : O(n)

        """
        # use two pointer methods

        # step 1 : 0이 아닌 값들을 모두 nums의 왼쪽으로 몰아 넣음
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1

        # step 2 : 왼쪽으로 몰아 넣을 때 원래 0이 아닌 원소들의 값 그대로 존재
        # -> 0으로 바꿔주는 작업
        while i < len(nums):
            nums[i] = 0
            i += 1
