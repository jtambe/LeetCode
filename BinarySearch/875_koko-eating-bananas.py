from typing import List, math

# https://www.youtube.com/watch?v=U2SozAs9RzA&t=16s

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r

        while(l <= r):
            mid = (l+r)//2
            hours = self.hours(piles, mid)
            if hours <= h:
                res = min(res, mid)
                r = mid-1
            else:
                l = mid+1

        return res


    def hours(self, piles: List[int], k: int) -> int:
        hours = sum([math.ceil(x/k) for x in piles])
        return hours