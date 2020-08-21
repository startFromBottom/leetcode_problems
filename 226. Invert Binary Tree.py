"""

problem link: https://leetcode.com/problems/invert-binary-tree/

"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        iterative - top down
        """
        q = deque([root])
        while q:
            node = q.pop()
            if node:
                node.left, node.right = node.right, node.left
                q.appendleft(node.left)
                q.appendleft(node.right)

        return root

    def invertTreeRecursive(self, root: TreeNode) -> TreeNode:
        """
        recursive - bottom up
        """
        if root:
            root.left, root.right = self.invertTreeRecursive(root.right), \
                                    self.invertTreeRecursive(root.left)
        return root
