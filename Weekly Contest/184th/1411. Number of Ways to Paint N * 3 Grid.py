"""

problem link : https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
submission detail : https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/submissions

"""


class Solution:
    """

    Use Dynamic Programming

    Time Complexity : O(n)
    Space Complexity : O(1)

    """
    def numOfWays(self, n: int) -> int:
        """
        last2 : 맨 마지막 행이 두 가지 색깔로 색칠되는 경우
        last3 : 맨 마지막 행이 세 가지 색깔로 색칠되는 경우

        두 경우로 나누어 점화식을 세운다.

        """
        last2_memo, last3_memo = [6], [6]
        for i in range(n - 1):
            last3 = 2 * last2_memo[-1] + 3 * last3_memo[-1]
            last2 = 2 * last2_memo[-1] + 2 * last3_memo[-1]

            last2_memo[-1] = last2
            last3_memo[-1] = last3

        return (last2_memo[-1] + last3_memo[-1]) % (10 ** 9 + 7)
