"""
problem link : https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3283/

"""
from typing import List

class Solution:
    """

    XOR 비트 연산을 활용

    XOR 연산이 교환법칙이 성립하기 때문에,
    같은 놈들 끼리 XOR 연산 했을 때 0이 되고,
    1개 남은 놈과 0 을 XOR 연산 했을 때 1개 남은 놈이 됨

    Time Complexity : O(n)
    Space Complexity : O(1)

    """
    def singleNumber(self, nums: List[int]) -> int:

        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i] # ^ : xor 연산
        return ans

print(2 ^ 0)