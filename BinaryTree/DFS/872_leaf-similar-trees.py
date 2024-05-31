from typing import Optional, Deque, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        q1 = deque()
        q2 = deque()

        def dfs(root: TreeNode, q: Deque):
            if root is None:
                return
            if(root.left is None and root.right is None):
                q.append(root.val)
                return
            dfs(root.left, q)
            dfs(root.right, q)

        dfs(root1, q1)
        dfs(root2, q2)

        if(len(q1) != len(q2)):
            return False
        
        while(len(q1) > 0):
            item1 = q1.popleft()
            item2 = q2.popleft()
            if(item1 != item2):
                return False
        
        return True