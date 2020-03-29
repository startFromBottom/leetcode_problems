"""

problem link : https://leetcode.com/problems/find-lucky-integer-in-an-array/
submission detail : https://leetcode.com/contest/weekly-contest-182/submissions/detail/316941656/

"""

from collections import Counter
from typing import List


class Solution:
    """
    Time Complexity : O(n)

    """

    def findLucky(self, arr: List[int]) -> int:

        c = Counter(arr)
        max_lucky_num = -1

        for k, v in c.items():
            if k == v:
                max_lucky_num = max(max_lucky_num, v)
        return max_lucky_num
