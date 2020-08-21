"""

problem link : https://leetcode.com/problems/diameter-of-binary-tree/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def traverse(root: TreeNode) -> int:
            if not root:
                return -1

            left = traverse(root.left)
            right = traverse(root.right)

            self.diameter = max(self.diameter, left + right + 2)

            return max(left, right) + 1

        traverse(root)

        return self.diameter
