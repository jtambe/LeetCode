# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if(head is None or head.next is None):
            return head

        # Get dummy head before head
        dummy = ListNode()
        dummy.next = head

        # get two pointers
        prev = dummy
        cur = head
        while(cur and cur.next):
            self.swap_pair(cur, cur.next, prev) # Swap two pointers, use prev
            prev = cur
            cur = cur.next

        # Return new head
        return dummy.next
        
    # Swap two nodes and use prev to link prev linkedList to new swaped pair
    def swap_pair(self, x: ListNode, y: ListNode, prev: ListNode) -> Optional[ListNode]:
        c = y.next # c = 3
        y.next = x # 2.next = 1
        x.next = c # 1.next = 3
        prev.next = y # dummy.next = 2

        