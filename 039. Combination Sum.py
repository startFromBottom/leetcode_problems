"""

problem link : https://leetcode.com/problems/combination-sum/
submission detail : https://leetcode.com/submissions/detail/312025851/

"""
from typing import List


class Solution:
    """

    Time Complexity: O(2 ** n)

    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates) - 1
        ans = []

        def comb_sum(sol: List[int], idx: int, current: int, target: int):
            if target == current:
                ans.append(sol)
                return
            if idx > n or current > target:
                return
            # use candidates[idx]
            comb_sum(sol + [candidates[idx]], idx, current + candidates[idx], target)
            # not use candidates[idx] -> idx + 1
            comb_sum(sol, idx + 1, current, target)

        comb_sum(sol=[], idx=0, current=0, target=target)

        return ans
