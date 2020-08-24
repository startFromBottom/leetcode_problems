"""

problem link : https://leetcode.com/problems/reconstruct-itinerary/submissions/

"""

from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)

        for f, t in sorted(tickets, reverse=True):
            graph[f].append(t)

        visited = []

        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            visited.append(node)

        dfs("JFK")

        return visited[::-1]

    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)
        for f, t in sorted(tickets, reverse=True):
            graph[f].append(t)

        visited = []
        stack = ["JFK"]

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            visited.append(stack.pop())

        return visited[::-1]
