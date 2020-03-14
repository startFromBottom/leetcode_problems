from typing import List, Tuple, Any
from itertools import combinations

"""

problem link : https://leetcode.com/problems/combinations/submissions/
submission detail : https://leetcode.com/problems/combinations/submissions/


"""


class Solution1:
    """
    use recursive strategy
    Time Complexity : ?

    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def recursion(case: List[int], sel_cnt: int, num: int):
            if sel_cnt == k:
                answer.append(case)
                return
            if num == n + 1:
                return
            # use num
            recursion(case + [num], sel_cnt + 1, num + 1)
            # not use num
            recursion(case, sel_cnt, num + 1)

        recursion([], 0, 1)

        return answer


class Solution2:
    """
    use itertools.combinations
    faster than solution 1

    """

    def combine(self, n: int, k: int) -> List[Tuple[Any, ...]]:
        return list(combinations(range(1, n + 1), k))
