from typing import Optional, List, Deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return root

        ans = [root.val]
        q = Deque()
        q.append(root)
        while(q):
            level = []
            for i in range(len(q)):
                item = q.popleft()
                if(item.left):
                    q.append(item.left)
                    level.append(item.left)
                if(item.right):
                    q.append(item.right)
                    level.append(item.right)

            if level:
                ans.append(level[-1].val)

        return ans            
        