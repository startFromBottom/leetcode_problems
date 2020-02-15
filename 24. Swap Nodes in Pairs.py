"""

problem link : https://leetcode.com/problems/swap-nodes-in-pairs/
submission detail : https://leetcode.com/submissions/detail/303462130/

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Time Complexity : O(n + n) = O(n)

    """

    def swapPairs(self, head: ListNode) -> ListNode:

        ans = ListNode("dummy")
        cur = ans
        node_vals = []  # save values of head ListNode
        swap_orders = []
        length = 0
        # part 1 : O(n)
        while head:
            if length % 2 == 0:
                swap_orders.append(length + 1)
            else:
                swap_orders.append(length - 1)
            node_vals.append(head.val)
            head = head.next
            length += 1
        if length % 2 == 1:
            swap_orders[-1] -= 1
        # part 2 : O(n)
        for idx in swap_orders:
            cur.next = ListNode(node_vals[idx])
            cur = cur.next

        return ans.next
