from collections import defaultdict
from typing import List


class Solution:
    """

    Time Complexity : O(n * m)
    n : length of strs
    m : average length of each string

    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)

        return ans.values()
