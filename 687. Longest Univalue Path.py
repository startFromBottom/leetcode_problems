"""

problem link : https://leetcode.com/problems/longest-univalue-path/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    length = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:

        def traverse(node: TreeNode) -> int:
            if not node:
                return 0

            left = traverse(node.left)
            right = traverse(node.right)

            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0

            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0

            self.length = max(self.length, left + right)

            return max(left, right)

        traverse(root)

        return self.length
