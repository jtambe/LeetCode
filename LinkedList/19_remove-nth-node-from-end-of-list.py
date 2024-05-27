
from typing import Optional
#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sizeOfList(self, head: ListNode) -> int:
        count = 1
        node = head
        while(node.next):
            count = count + 1
            node = node.next
        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.sizeOfList(head)

        # since we know that removeIndex is smaller or equal to length
        if length == 1:
            return None

        removeIndex = length - n + 1
        if removeIndex == 1:
            head = head.next
            return head

        curIndex = 1
        prev, cur, next = head, head, head.next
        while(curIndex < removeIndex):
            prev = cur
            cur = next
            next = next.next
            curIndex = curIndex + 1
        
        prev.next = next

        return head



    
        