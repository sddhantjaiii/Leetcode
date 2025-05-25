import heapq
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-x for x in piles]  # Use negatives to simulate max-heap
        heapq.heapify(max_heap)
        print(max_heap)
        while k > 0:
            largest = -heapq.heappop(max_heap)
            reduced = (largest // 2)
            heapq.heappush(max_heap, -(largest - reduced))
            k -= 1

        return -sum(max_heap)
