"""

problem link : https://leetcode.com/problems/permutations-ii/
submission detail : https://leetcode.com/problems/permutations-ii/submissions/

"""
from typing import List


class Solution1:
    """
    Based on 046. Permutations Solution
    Time Complexity: O(n!)
    """

    def permuteUnique(self, nums: List[int]) -> List[int]:
        ans = set()

        def recursion(nums: List[int], arr: List[int]):
            if not nums and tuple(arr) not in ans:
                ans.add(tuple(arr))
                return
            for i in range(len(nums)):
                recursion(nums[:i] + nums[i + 1:], arr + nums[i])

        recursion(nums, [])

        return list(ans)


class Solution2:
    """

    Slightly faster than Solution 1

    This is because there is no need to partially search for duplicates through filtering.

    Time Complexity: O(n!) (Worst Case)

    """

    def permuteUnique(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()

        def recursion(nums: List[int], arr: List[int]):
            if not nums:
                ans.append(nums)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                recursion(nums[:i] + nums[i + 1:], arr + [nums[i]])

        recursion(nums, [])
        return ans
