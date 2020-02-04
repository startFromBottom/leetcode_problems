"""
problem link : https://leetcode.com/problems/longest-substring-without-repeating-characters/

solution1 submission detail : https://leetcode.com/submissions/detail/299886396/
solution2 submission detail : https://leetcode.com/submissions/detail/299888733/
"""


# solution 1 : Sliding Window
# Time Complexity : O(2n) = O(n), (n : length of s)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_sets = set()
        ans = 0
        i = 0
        j = 0
        while i < n and j < n:
            if s[j] not in char_sets:
                char_sets.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                char_sets.remove(s[i])
                i += 1


# solution 2: Sliding Window Optimization
# Time Complexity : O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        char_dict = dict()  # current index of character
        i = 0
        for j in range(n):
            if s[j] in char_dict.keys():
                i = max(char_dict.get(s[j]), i)
            ans = max(ans, j - i + 1)
            char_dict[s[j]] = j + 1
        return ans
