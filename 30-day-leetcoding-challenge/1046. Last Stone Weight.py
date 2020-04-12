"""

problem link : https://leetcode.com/problems/last-stone-weight/
submission detail : https://leetcode.com/problems/last-stone-weight/submissions


"""

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    """

    Time Complexity : O(n)

    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = len(stones)
        # make max heap
        h = [(-s, s) for s in stones]  # (priority, value)
        heapify(h)
        while l > 1:
            first = heappop(h)[1]
            second = heappop(h)[1]
            if first != second:
                dif = abs(first - second)
                heappush(h, (-dif, dif))
                l -= 1
            else:  #
                l -= 2
        if not h:
            return 0
        return heappop(h)[1]