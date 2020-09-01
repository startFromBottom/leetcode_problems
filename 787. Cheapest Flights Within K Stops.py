"""

problem link : https://leetcode.com/problems/cheapest-flights-within-k-stops/

"""

from collections import defaultdict
from typing import List
import heapq


class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # price, vertex, travel_cnt
        Q = [(0, src, 0)]
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k <= K:
                k += 1
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k))
        return -1