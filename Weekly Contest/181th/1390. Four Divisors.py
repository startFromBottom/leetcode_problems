"""

problem link : https://leetcode.com/problems/four-divisors/
submission detail : https://leetcode.com/problems/four-divisors/submissions

"""
from typing import List


class Solution:
    """

    Time Complexity : O( n * (m * 0.5))
    n : length of nums
    m : size of number

    """

    def sumFourDivisors(self, nums: List[int]) -> int:

        divisors = []

        def check_four_divisors(num: int):
            divisors = []
            cnt = 0
            i = 1
            while i <= num ** 0.5:
                if num % i == 0:
                    other = num // i
                    if other == i:
                        divisors.extend([i])
                        cnt += 1
                    else:
                        divisors.extend([i, other])
                        cnt += 2
                i += 1
            if cnt == 4:
                return divisors
            return False

        for num in nums:
            res = check_four_divisors(num)
            if res:
                divisors.extend(res)

        return sum(divisors)