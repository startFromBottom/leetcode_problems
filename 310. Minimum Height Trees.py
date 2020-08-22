"""

problem link : https://leetcode.com/problems/minimum-height-trees/

"""

from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]

        # step 1 : make graph
        graph = defaultdict(set)
        for (x, y) in edges:
            graph[x].add(y)
            graph[y].add(x)

        # step 2 : find leaves
        leaves = []
        for node, next_nodes in graph.items():
            if len(next_nodes) == 1:
                leaves.append(node)

        # step 3 : delete leaves in graphs iteratively
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
