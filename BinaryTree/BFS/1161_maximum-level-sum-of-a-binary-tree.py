from typing import Optional, Deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        q = Deque()
        q.append(root)
        levelSum = [root.val]
        while(q):
            level = []
            for i in range(len(q)):
                item = q.popleft()
                if(item.left):
                    q.append(item.left)
                    level.append(item.left.val)
                if(item.right):
                    q.append(item.right)
                    level.append(item.right.val)
            if level:
                levelSum.append(sum(level))

        print(levelSum)
        maxSum = max(levelSum)
        for idx, x in enumerate(levelSum):
            if x == maxSum:
                return idx+1

        


        