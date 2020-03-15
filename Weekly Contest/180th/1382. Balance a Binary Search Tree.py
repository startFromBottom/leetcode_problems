""""

problem link : https://leetcode.com/problems/balance-a-binary-search-tree/
submission detail : https://leetcode.com/problems/balance-a-binary-search-tree/submissions/

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """

    Time Complexity: O(n + n) = O(n)
    n : # of nodes

    """
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def store_nodes(root: TreeNode):
            if not root:
                return
            store_nodes(root.left)
            nodes.append(root)
            store_nodes(root.right)

        store_nodes(root)
        n = len(nodes)

        def make_balance_recursion(start: int, end: int) -> TreeNode:
            if start > end:
                return
            mid = (start + end) // 2
            node = nodes[mid]
            node.left = make_balance_recursion(start, mid - 1)
            node.right = make_balance_recursion(mid + 1, end)

            return node

        return make_balance_recursion(0, n - 1)
