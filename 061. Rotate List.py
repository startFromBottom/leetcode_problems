"""

problem link : https://leetcode.com/problems/rotate-list/
submission detail : https://leetcode.com/submissions/detail/309213233/

discussion link

1) link-and-break strategy : https://leetcode.com/problems/rotate-list/discuss/466395/Python-O(-n-)-sol.-by-link-and-break-strategy-93%2B-With-explanation
2) Python 99% (24ms) 100% memory with comments : https://leetcode.com/problems/rotate-list/discuss/481684/Python-99-(24ms)-100-memory-with-comments

"""


class ListNode:
    def __init__(self, x: int):
        self.val: int = x
        self.next: ListNode = None


class Solution1:
    """
    1) link-and-break strategy

    Time-Complexity : O(n) (n : length of linked-list)
    """

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None

        # step 1
        # connect tail and head, make a circular link
        cur, size = head, 1
        while cur.next:
            size += 1
            cur = cur.next
        # link
        cur.next = head
        # step 2
        # locate the new head after rotation, and break the circle
        r = size - (k % size)
        cur = head
        for i in range(1, r):
            cur = cur.next
        new_head_after_rotation = cur.next
        # break
        cur.next = None

        return new_head_after_rotation


class Solution2:
    """
    2)
    Time Complexity: O(n) (n : length of linked list)
    """
    def get_length(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # handle the situations don't need to rotate
        n = self.get_length(head)
        if n <= 1:
            return head
        k = k % n

        if k == 0:
            return head

        # [1,2,3,4,5]
        # since we already have the length, we go straight to the node instead of using two pointer
        slow = head
        for _ in range(n-k-1):
            slow = slow.next

        # record the latter part would be swapped
        # remember to use two variables (prev, curr) because the curr need to travel down the last node
        prev = slow.next
        curr = slow.next
        slow.next = None
        while curr:
            curr = curr.next
        curr.next = head
        return prev
