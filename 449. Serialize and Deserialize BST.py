"""

problem link : https://leetcode.com/problems/serialize-and-deserialize-bst/

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, n):
        """Encodes a tree to a single string.
        """
        return None if not n else [n.val, self.serialize(n.left), self.serialize(n.right)]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """
        if data:
            val, left, right = data
            n = TreeNode(val)
            n.left = self.deserialize(left)
            n.right = self.deserialize(right)
            return n
        # return None is implicit
