"""

problem link : https://leetcode.com/problems/design-a-stack-with-increment-operation/
submission detail : https://leetcode.com/contest/weekly-contest-180/submissions/detail/312523179/

"""


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        try:
            return self.stack.pop()
        except IndexError as e:
            return -1

    def increment(self, k: int, val: int) -> None:
        try:
            for i in range(k):
                self.stack[i] += val
        except IndexError as e:
            return


