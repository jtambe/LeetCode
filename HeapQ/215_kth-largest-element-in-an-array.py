from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxheap = [x*-1 for x in nums]
        heapq.heapify(maxheap) # O(n)

        for i in range(k-1):
            heapq.heappop(maxheap)
        
        return maxheap[0]*-1

        