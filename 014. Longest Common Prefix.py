"""

problem link : https://leetcode.com/problems/longest-common-prefix/
submission detail : https://leetcode.com/problems/longest-common-prefix/submissions/

"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        ans = ""
        min_length = min([len(s) for s in strs])

        for i in range(min_length):
            temp = strs[0][:i + 1]
            for s in strs:
                if temp != s[:i + 1]:
                    return ans
            ans = temp

        return strs[0][:min_length]