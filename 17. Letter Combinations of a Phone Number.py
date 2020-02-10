"""

problem link : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
submission detail : https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

"""
from typing import List


class Solution:
    """
    Time Complexity : O(x ** n)
    x : 3 or 4
    n : min 1 , max 8

    use bottom-up dynamic programming
    """

    digit_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:

        # part 1: check input
        if len(digits) == 0:
            return []
        for digit in digits:
            if digit not in self.digit_to_letters:
                return []

        # part 2 : solve problem
        # use bottom-up dynamic programming
        length = len(digits)
        first = digits[0]
        ans = list(self.digit_to_letters[first])
        for i in range(1, length):
            ans = [s1 + s2 for s1 in ans for s2 in self.digit_to_letters[digits[i]]]

        return ans
