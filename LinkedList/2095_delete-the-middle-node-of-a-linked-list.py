
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        l = 0
        cur = head
        while(cur):
            l += 1
            cur = cur.next

        if l < 2:
            return None

        mid = l//2
        l = 0
        left = ListNode()
        right = head
        while(right):
            if l == mid:
                left.next = right.next
                break
            left = right
            right = right.next                
            l += 1

        return head

        