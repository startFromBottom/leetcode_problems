"""

problem link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
submission detail : https://leetcode.com/submissions/detail/304153988/

"""
from typing import List


class Solution:
    """

    Time Complexity : O(n)

    """

    def maxProfit(self, prices: List[int]) -> int:
        min_price = 2 ** 32 - 1
        max_profit = 0
        for i, v in enumerate(prices):
            if v < min_price:
                min_price = v
            elif v - min_price > max_profit:
                max_profit = v - min_price
        return max_profit
