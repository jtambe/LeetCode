# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        even = ListNode()
        evenFirst = even
        odd = ListNode()
        oddFirst = odd
        cur = head
        i = 1
        while(cur):
            if(i % 2 == 0):
                even.next = cur
                even = even.next
            else:
                odd.next = cur
                odd = odd.next
            i += 1
            cur = cur.next
        odd.next = evenFirst.next
        even.next = None
        return oddFirst.next
        