
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.minheap = [x for x in range(1,1001)]
        heapq.heapify(self.minheap)
        self.minheapset = set(self.minheap)
        

    def popSmallest(self) -> int:
        num = heapq.heappop(self.minheap)
        self.minheapset.remove(num)
        return num

    def addBack(self, num: int) -> None:
        if num in self.minheapset:
            return
        else:
            heapq.heappush(self.minheap, num)
            self.minheapset.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)