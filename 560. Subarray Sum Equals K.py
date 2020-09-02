"""

problem link : https://leetcode.com/problems/subarray-sum-equals-k/solution/

"""

from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        cur_sum = 0
        d = defaultdict(int)
        for i, num in enumerate(nums):
            cur_sum += num
            if cur_sum == k:
                ans += 1
            if cur_sum - k in d:
                ans += d[cur_sum - k]
            d[cur_sum] += 1
        return ans
