# https://www.youtube.com/watch?v=Al6TW2WErK8
from typing import List,Deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        if root is None: return []
        
        q = Deque()
        output = []

        q.appendleft(root)

        while(q):
            
            cur = q.popleft()
            output.append(cur.val)

            for child in reversed(cur.children):
                q.appendleft(child)

        return output





        # output = []
        # def dfs(root: Node):
            
        #     if root is None:
        #         return

        #     output.append(root.val)
        #     for child in root.children:
        #         dfs(child)
        
        # dfs(root)
        # return output