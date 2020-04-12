"""

problem link : https://leetcode.com/problems/queries-on-a-permutation-with-key/
submission detail : https://leetcode.com/problems/queries-on-a-permutation-with-key/submissions

"""

from typing import List


class Solution:
    """

    Time Complexity : O(n^2)

    """
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = []
        P = list(range(1, m + 1))  # [1,2,3,4,5]
        for i in range(len(queries)):
            pos = P.index(queries[i])
            ans.append(pos)
            P = [P[pos]] + P
            del P[pos + 1]
        return ans