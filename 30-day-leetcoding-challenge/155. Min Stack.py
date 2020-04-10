"""

problem link : https://leetcode.com/problems/min-stack/
submission detail : https://leetcode.com/problems/min-stack/submissions


"""


class MinStack:
    """

    all Time Complexity : O(1)

    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = -99999999999999

    def push(self, x: int) -> None:

        if not self.stack:
            self.min_val = x
        else:
            self.min_val = min(self.min_val, x)

        self.stack.append((x, self.min_val))

    def pop(self) -> None:
        try:
            self.stack.pop()
            self.min_val = self.stack[-1][1]
        except IndexError:
            print("stack is empty")

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
