"""

problem link : https://leetcode.com/problems/longest-happy-prefix/submissions/
submission detail : https://leetcode.com/submissions/detail/314825759/

"""


class Solution:
    """

    Time Complexity : O(n)

    """
    def longestPrefix(self, s: str) -> str:
        N = len(s)
        candidates = ""
        for i in range(N):
            if s[:i] == s[-i:]:
                candidates = s[:i]

        return candidates