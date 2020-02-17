"""
problem link : https://leetcode.com/problems/add-two-numbers/
submission detail : https://leetcode.com/submissions/detail/288934129/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_ListNode_val(l: ListNode) -> list:
    num_list = []
    while l.next != None:
        num_list.append(l.val)
        l = l.next
    # add last
    num_list.append(l.val)

    return num_list


def connect_ListNodes(node_list: list) -> ListNode:
    if len(node_list) == 1:
        return node_list[0]

    node_list[0].next = node_list[1]
    for i in range(1, len(node_list)):
        node_list[i - 1].next = node_list[i]
    return node_list[0]


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = add_ListNode_val(l1)
        num2 = add_ListNode_val(l2)

        num1.reverse()
        num2.reverse()

        two_sum = str(int("".join(map(str, num1))) + int("".join(map(str, num2))))
        node_list = [ListNode(two_sum[i]) for i in range(len(two_sum) - 1, -1, -1)]

        answer = connect_ListNodes(node_list)

        return answer
