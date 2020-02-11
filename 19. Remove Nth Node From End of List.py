"""

problem_link : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
submission detail : https://leetcode.com/submissions/detail/302278844/

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Use Two pointer,
    solve problem in one pass

    Time Complexity : O(n) (n : length of linked list)

    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if not head or not head.next:
            return

        # make dummy ListNode
        dummy = ListNode(0)
        dummy.next = head
        # two pointers
        first = dummy
        second = dummy
        # advance first pointer so that the gap between first and second is n nodes apart
        for _ in range(n + 1):
            first = first.next
        # move first to the end, maintaing the gap
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next
