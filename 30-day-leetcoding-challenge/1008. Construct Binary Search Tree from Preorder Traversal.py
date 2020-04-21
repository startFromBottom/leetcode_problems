"""

problem link : https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
submission detail : https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/submissions

"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    """

    Time Complexity : O(nlogn)

    n -> for문 돌면서..
    logn -> Tree의 특정 지점에 값 할당

    """

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        root = TreeNode(preorder[0])

        def construct_preorder(root, v):
            if v < root.val:
                if root.left is not None:
                    construct_preorder(root.left, v)
                else:
                    root.left = TreeNode(v)
            else:
                if root.right is not None:
                    construct_preorder(root.right, v)
                else:
                    root.right = TreeNode(v)

        for i in range(1, len(preorder)):
            start = root
            construct_preorder(start, preorder[i])

        return root


class Solution2:
    """

    Time Complexity : ?

    """

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return
        val = preorder[0]
        i = 1
        while i < len(preorder):
            if preorder[i] < val:
                i += 1
            else:
                break
        root = TreeNode(val)
        left, right = preorder[1:i], preorder[i:]
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)

        return root
