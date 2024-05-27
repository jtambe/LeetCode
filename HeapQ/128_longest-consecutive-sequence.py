import heapq
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # if we have single or no element, return the length
        if(len(nums) <=1):
            return len(nums)

        # create a set of numbers because, they may contain duplicate numbers which will reset the maxLength counter
        minheap = list(set(nums))
        # create a minheap of unique numbers
        #heapify when used as botton-up approach, runs in O(n)
        heapq.heapify(minheap)

        #create a logic to keep popping numbers from minheap and verify if they consecutive
        maxLength = 1
        cur = heapq.heappop(minheap)
        curLength = 1
        while(len(minheap) > 0):
            next = heapq.heappop(minheap)

            # if popped number is consecutive, update current Length and maxLength
            if(next == cur+1):
                curLength = curLength+1
                maxLength = max(curLength, maxLength)
            # otherwise, reset the current Length variable
            else:
                curLength = 1
            
            #in all cases, update the current to next for further comparison
            cur = next
        
        return maxLength