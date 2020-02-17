"""

problem link : https://leetcode.com/problems/implement-strstr/submissions/
submission detail : https://leetcode.com/submissions/detail/303468944/

"""


class Solution:
    """

    Time Complexity : O(n)

    """
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        ans = -1
        length = len(needle)
        for i in range(len(haystack)):
            substr = haystack[i:i + length]
            if substr == needle:
                return i

        return ans
