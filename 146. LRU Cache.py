"""

problem link : https://leetcode.com/problems/lru-cache/

"""


class Node:
    """
    Doubly Linked List

    """

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node: Node):
        """
        add node in tail.prev
        """
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def get(self, key: int) -> int:
        if key in self.cache:
            cur_node = self.cache[key]
            self._remove(cur_node)
            self._add(cur_node)
            return cur_node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        cur_node = Node(key, value)
        self._add(cur_node)
        self.cache[key] = cur_node
        if len(self.cache) > self.size:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]
