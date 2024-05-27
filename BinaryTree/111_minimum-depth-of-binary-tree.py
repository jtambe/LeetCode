# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if(root is None):
            return 0

        def helper(root: TreeNode, height: int) -> int:
            
            height = height +1
            
            # return height if it is leaf node
            if(root and root.left is None and root.right is None):
                return height

            # otherwise check conditions
            if(root.left and root.right is None):
                return helper(root.left, height)
            if(root.right and root.left is None):
                return helper(root.right, height)
            return min(helper(root.left, height), helper(root.right, height))
        
        return helper(root, 0)
        