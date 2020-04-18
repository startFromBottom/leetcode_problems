"""

problem link : https://leetcode.com/problems/middle-of-the-linked-list/
submission detail : https://leetcode.com/problems/middle-of-the-linked-list/submissions/

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

    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast:
            fast = fast.next.next
            slow = slow.next
        return slow
