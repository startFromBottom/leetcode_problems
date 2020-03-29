"""

problem link : https://leetcode.com/problems/count-number-of-teams/
submission detail : https://leetcode.com/contest/weekly-contest-182/submissions/detail/316955114/


"""

from typing import List


class Solution:
    """

    Time Complexity: O(n C 3 ) = O(n**3)

    """

    def numTeams(self, rating: List[int]) -> int:
        ans = []

        def recursion(arr, i):

            if len(arr) == 3:
                if arr[0] < arr[1] < arr[2] or arr[2] < arr[1] < arr[0]:
                    ans.append(arr)
                return
            if i == len(rating):
                return

            recursion(arr + [rating[i]], i + 1)
            recursion(arr, i + 1)

        recursion([], 0)

        return len(ans)
