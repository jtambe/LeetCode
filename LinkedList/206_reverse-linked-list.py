
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if(head is None):
            return head

        # push nodes in a stack
        mystack = []
        curNode = head
        while(curNode is not None):
            mystack.append(curNode)
            curNode = curNode.next

        # pop each node until stack is empty and recreate list
        head = mystack.pop()
        curNode = head
        while(len(mystack) > 0):
            popped = mystack.pop()
            popped.next = None # important step to avoid cycle
            curNode.next = popped
            curNode = popped
        
        #curNode = None

        return head


        