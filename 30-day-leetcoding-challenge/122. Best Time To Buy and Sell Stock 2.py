"""

problem link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
submission detail : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/

"""
from typing import List


class Solution:
    """

    Time Complexity : O(n)

    """

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = 2 ** 32 - 1
        for i, p in enumerate(prices):
            if p >= min_price:
                profit += p - min_price
            min_price = p
        return profit
