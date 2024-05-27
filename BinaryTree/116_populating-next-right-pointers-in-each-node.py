"""
Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from typing import Optional, deque


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is None:
            return root

        q = deque()
        q.append(root)
        while(any(q)):
            #create level deque
            cur = deque()
            while(any(q)):
                cur.append(q.popleft())
            
            #get 1st element from current level and append its children in q
            l = cur.popleft()
            if l.left:
                q.append(l.left)
            if l.right:
                q.append(l.right)

            # while there are any more elements in current level, pop them and append its children
            # then move the left and right pointers to further move in the list
            while(any(cur)):
                r = cur.popleft()
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
                l.next = r
                l = r


        return root