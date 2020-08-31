"""

problem link : https://leetcode.com/problems/network-delay-time/


"""

from collections import defaultdict
from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = defaultdict(int)
        Q = [(0, K)]  # time, vertex
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = w + time
                    heapq.heappush(Q, (alt, v))

        if len(dist) == N:
            return max(dist.values())
        return -1
