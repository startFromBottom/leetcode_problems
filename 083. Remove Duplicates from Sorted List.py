"""

problem link : https://leetcode.com/problems/remove-duplicates-from-sorted-list/
submission detail : https://leetcode.com/submissions/detail/313014979/ 

"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Time Complexity : O(n)

    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head