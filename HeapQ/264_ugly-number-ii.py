import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minheap = [1]
        heapq.heapify(minheap)
        i = 0
        uglyNums = set([])
        while(i < n - 1):
            cur = heapq.heappop(minheap)
            uglyNums.add(cur)
            mul = cur*2
            if(mul not in uglyNums):
                heapq.heappush(minheap, mul)
                uglyNums.add(mul)
            mul = cur*3
            if(mul not in uglyNums):
                heapq.heappush(minheap, mul)
                uglyNums.add(mul)
            mul = cur*5
            if(mul not in uglyNums):
                heapq.heappush(minheap, mul)
                uglyNums.add(mul)
            i = i+1
        
        return minheap[0]