"""

problem link : https://leetcode.com/problems/reverse-linked-list/
submission detail : https://leetcode.com/submissions/detail/309534265/

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    my first solution

    Time Complexity : O(2*n) = O(n)
    n : length of linked list

    """
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        values = []
        length = 0
        while cur:
            values.append(cur.val)
            cur = cur.next
            length += 1

        dummy = ListNode("dummy")
        cur = dummy
        for i in range(length - 1, -1, -1):
            cur.next = ListNode(values[i])
            cur = cur.next

        return dummy.next


class Solution2:
    """
    faster than solution1 (iterative solution)

    Time Complexity : O(n)
    Space Complexity : O(1)
    n : length of linked list

    """
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev


class Solution3:
    """
    faster than solution1 (recursive solution)

    Time Complexity : O(n)
    Space Complexity: O(n) - The extra space comes from implicit stack space due to recursion.
    n : length of linked list

    """
    def reverseList(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
