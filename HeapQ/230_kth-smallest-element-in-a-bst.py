# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
import heapq
from typing import deque, Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # create a minheap
        minheap = []
        heapq.heapify(minheap)

        # basic BFS traversal
        q = deque()
        q.append(root)
        while(any(q)):
            item = q.popleft()
            if(item):
                heapq.heappush(minheap, item.val)
                q.append(item.left)
                q.append(item.right)
        
        # Get kth element                
        i = 0
        while(i < k-1):
            heapq.heappop(minheap)
            i += 1
        return minheap[0]





        