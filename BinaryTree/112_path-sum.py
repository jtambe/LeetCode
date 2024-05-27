# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if(root is None):
            return False

        def helper(root: TreeNode, currentSum: int) -> bool:
            if(root is None):
                return False
            if(root.left is None and root.right is None and targetSum == currentSum + root.val):
                return True

            return helper(root.left, currentSum + root.val) or helper(root.right, currentSum + root.val)

        return helper(root, 0)


        

        