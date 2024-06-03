
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        a = []
        cur = head
        while(cur):
            a.append(cur.val)
            cur = cur.next
        
        if len(a) == 2:
            return sum(a)

        maxSum = 0
        l,r = 0,len(a)-1
        while(l < r):
            maxSum = max(a[l]+a[r], maxSum)
            l += 1
            r -= 1

        return maxSum