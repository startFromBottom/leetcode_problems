"""

problem link : https://leetcode.com/problems/merge-two-sorted-lists/
submission detail : https://leetcode.com/submissions/detail/302292901/

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    use dummy ListNode
    Time Complexity : O(len(l1) + len(l2))
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # make initial value
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2

        return dummy.next
