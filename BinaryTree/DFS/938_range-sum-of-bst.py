from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        global curSum
        curSum = 0
        def dfs(root: TreeNode):
            if root and root.val <= high and root.val >= low:
                global curSum
                curSum += root.val
            if root is None:
                return
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)

        return curSum

        