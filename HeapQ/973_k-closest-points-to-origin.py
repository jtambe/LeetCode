
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        d = [((x[0]*x[0] + x[1]*x[1]), x)  for x in points]
        heapq.heapify(d)

        ans = []
        while(k > 0 and d):
            item = heapq.heappop(d)
            ans.append(item[1])
            k -= 1

        return ans


        