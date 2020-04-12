"""

problem link : https://leetcode.com/problems/string-matching-in-an-array/
submission detail : https://leetcode.com/problems/string-matching-in-an-array/submissions

"""

from typing import List


class Solution:
    """

    Time Complexity : O(n ** 2)

    """

    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    ans.append(words[i])
        return list(set(ans))