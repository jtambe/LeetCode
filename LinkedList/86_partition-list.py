# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        #neetcode solution used
        #https://www.youtube.com/watch?v=KT1iUciJr4g

        leftList, rightList = ListNode(), ListNode()
        ltail, rtail = leftList, rightList

        cur = head
        while(cur):
            if(cur.val < x):
                ltail.next = cur
                ltail = ltail.next
            else:
                rtail.next = cur
                rtail = rtail.next
            cur = cur.next
        
        ltail.next = rightList.next
        rtail.next = None

        return leftList.next





        