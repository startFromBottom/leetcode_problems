"""

problem link : https://leetcode.com/problems/combination-sum-ii/
submission detail : https://leetcode.com/problems/combination-sum-ii/submissions/

"""
from typing import List
from collections import Counter


class Solution1:
    """
    Runtime : 324ms

    Time Complexity : O(2**n)

    """

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates) - 1
        ans = set()

        def comb_sum2(sol: List[int], idx: int, current: int, target: int):
            if current == target:
                ans.add(tuple(sorted(sol)))
                return
            if idx > n or current > target:
                return
            comb_sum2(sol + [candidates[idx]], idx + 1, current + candidates[idx], target)
            comb_sum2(sol, idx + 1, current, target)

        comb_sum2([], 0, 0, target)

        return ans


class Solution2:
    """
    Rum time: 108ms
    Slightly Faster than Solution1

    Time Complexity: O(n**2)

    """

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        cand_counter = Counter(candidates)
        candidates = list(set(candidates))
        n = len(candidates) - 1

        def comb_sum2(sol: List[int], idx, same_cnt, current, target):
            if current == target:
                ans.append(sol)
                return
            if idx > n or current > target:
                return
            if same_cnt < cand_counter[candidates[idx]]:
                # can use same value
                comb_sum2(sol + [candidates[idx]], idx, same_cnt + 1, current + candidates[idx], target)
            comb_sum2(sol, idx + 1, 0, current, target)

        comb_sum2([], 0, 0, 0, target)

        return ans
