
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

    def reverseList_with_O1_space_complexity(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        cur = head
        prev = None

        while (cur):
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        
        return prev


        

from typing import List

class LinkedListNode:
  def __init__(self, val:int, next):
    self.val = val
    self.next = next
    
"""
Used stack approach instead
prev -> 1 -> 2 -> 3 -> 4

1 <- prev  2 -> 3 -> 4
1 <- 2 <- prev  3 -> 4
1 <- 2 <- 3 <- prev  4
1 <- 2 <- 3 <- 4 <- prev

4 
"""
    
def reverseList(head: LinkedListNode) -> LinkedListNode:
  
  if head is None:
    return head
    
  cur = head
  stack = []
  while cur:
    stack.append(cur)
    cur = cur.next
    
  head = stack.pop()
  cur = head
  while stack:
    nextItem = stack.pop()
    cur.next = nextItem
    cur = nextItem
  
  cur.next = None
  return head
  


def buildList(input:List[int]) -> LinkedListNode:
  n = len(input)
  head = None
  if n == 0:
    return head
    
  head = LinkedListNode(input[0], None)
  cur = head
  for i in range(1,n):
    cur.next = LinkedListNode(input[i], None)
    cur = cur.next
  
  return head
  
def TraverseList(head) -> List[int]:
  
  result = []
  if head is None:
    return result
  
  cur = head
  while(cur):
    result.append(cur.val)
    cur = cur.next
  
  return result
    
    


head = buildList([0,1,2,3])
cur = head
while cur:
  cur = cur.next
  
head = reverseList(head)
cur = head
result = TraverseList(head)
print(f"result:{result}")

head = buildList([])
cur = head
while cur:
  cur = cur.next

head = reverseList(head)
cur = head
result = TraverseList(head)
print(f"result:{result}")