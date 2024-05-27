# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional, deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return root

        q = deque()
        q.append(root)
        ans = []
        while(any(q)):
            cur = deque()
            while(any(q)):
                cur.append(q.popleft())
            ans.append([x.val for x in cur])
            while(any(cur)):
                n = cur.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right) 
            
             
        return ans
        