"""

problem link : https://leetcode.com/problems/two-sum/
submission detail : https://leetcode.com/submissions/detail/288925577/

"""

from typing import List


class Solution:
    """
    O(n**2) Solution
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return False


# 19.02.06 upload
class Solution:
    """
    O(n) Solution
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return dict[target - num], i
            dict[num] = i

        return False