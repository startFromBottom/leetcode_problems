"""

problem link : https://leetcode.com/problems/same-tree/
submission detail : https://leetcode.com/problems/same-tree/submissions/

"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Time Complexity : O(n)
    n : numbers of nodes

    """

    def bfs(self, t: TreeNode) -> List:

        q = deque([t])
        values = []
        while q:
            node = q.pop()
            if node is not None:
                values.append(node.val)
                # left
                if node.left is not None:
                    q.appendleft(node.left)
                else:
                    q.appendleft(None)
                # right
                if node.right is not None:
                    q.appendleft(node.right)
                else:
                    q.appendleft(None)
            else:
                values.append(None)

        return values

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.bfs(p) == self.bfs(q)