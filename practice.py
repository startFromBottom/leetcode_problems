from heapq import heapify, heappop, heappush
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    l = len(stones)
    # make max heap
    h = [(-s, s) for s in stones]  # (priority, value)
    heapify(h)
    while l > 1:
        first = heappop(h)[1]
        second = heappop(h)[1]
        if first != second:
            dif = abs(first - second)
            heappush(h, (-dif, dif))
            l -= 1
        else:  #
            l -= 2
    return heappop(h)[1]


print(lastStoneWeight([1, 3, 7, 9, 10]))
