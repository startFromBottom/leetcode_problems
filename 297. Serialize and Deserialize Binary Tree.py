"""

problem link : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

"""

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = deque([root])
        res = []
        while q:
            node = q.pop()
            if not node:
                res.append("#")
            else:
                res.append(node.val)
                q.appendleft(node.left)
                q.appendleft(node.right)

        return " ".join(list(map(str, res)))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(" ")
        if data == ["#"]:
            return None

        root = TreeNode(data[0])
        q = deque([root])
        i = 1

        while i < len(data) and q:
            node = q.pop()
            if data[i] != "#":
                node.left = TreeNode(data[i])
                q.appendleft(node.left)
            i += 1
            if data[i] != "#":
                node.right = TreeNode(data[i])
                q.appendleft(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
