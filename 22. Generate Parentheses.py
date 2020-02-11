"""

problem link : https://leetcode.com/problems/generate-parentheses/
submission detail : https://leetcode.com/submissions/detail/302314493/

"""
from typing import List


class Solution:
    """

    use backtracking
    description : https://leetcode.com/problems/generate-parentheses/solution/
    hard,,,
    """

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s="", left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)

        backtrack()
        return ans
