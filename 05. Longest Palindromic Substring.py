"""
problem link : https://leetcode.com/problems/longest-substring-without-repeating-characters/
submission detail : https://leetcode.com/submissions/detail/300106510/
"""


class Solution:
    """
    Time Complexity : O(n**2)
    n : length of s
    """

    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        ans = ""  # len 1 -> always palindrome
        for i in range(0, n):
            # check palindrome
            start = s[i]
            left = i - 1
            right = i + 1
            while left >= 0 and s[left] == start[0]:
                start = s[left] + start
                left -= 1
            while right <= n - 1 and s[right] == start[-1]:
                start = start + s[right]
                right += 1
            while left >= 0 and right <= n - 1 and s[left] == s[right]:
                start = s[left] + start + s[right]
                left -= 1
                right += 1
            if len(start) > len(ans):
                ans = start

        return ans
