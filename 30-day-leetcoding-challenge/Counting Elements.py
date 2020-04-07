"""

problem link : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/
submission detail :

"""

from collections import Counter
from typing import List


class Solution:
    """

    Time Complexity : O(nlogn)
    sorting 했기 때문

    """
    def countElements(self, arr: List[int]) -> int:

        ans = 0
        c = Counter(arr)
        keys = sorted(list(c.keys()))
        for i in range(1, len(keys)):
            if keys[i - 1] == keys[i] - 1:
                ans += c[keys[i - 1]]
        return ans
