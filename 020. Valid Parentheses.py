"""

problem link : https://leetcode.com/problems/valid-parentheses/
submission detail : https://leetcode.com/submissions/detail/302285164/

"""


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}

        for each in s:
            try:
                if each in bracket_map.values():
                    stack.append(each)
                elif stack[-1] != bracket_map[each]:
                    return False
                else:
                    stack.pop()
            except IndexError:
                return False

        if stack:
            return False
        return True
