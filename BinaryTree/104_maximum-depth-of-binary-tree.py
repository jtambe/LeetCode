# Definition for a binary tree node.
from typing import Optional
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        # if root.left is None and root.right is None:
        #     return 1

        def depth(root: TreeNode, height: int) -> int:
            if(root is None):
                return height
            # if(root.left is None):
            #     return depth(root.right, height+1)
            # if(root.right is None):
            #     return depth(root.left, height+1)
            return max(depth(root.left, height +1), depth(root.right, height+1))

        maxD = max(depth(root.left, 1), depth(root.right, 1))
        return maxD

        
        