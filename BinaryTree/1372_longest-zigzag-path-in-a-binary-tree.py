from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        LEFT, RIGHT = "left", "right"

        def dfs(root: TreeNode, curCount: int, prevSide: str) -> int:

            if (root is None):
                return curCount
            if prevSide == LEFT:
                return max(dfs(root.right, curCount+1, RIGHT), dfs(root.left, 0, LEFT), curCount)
            if prevSide == RIGHT:
                return max(dfs(root.left, curCount+1, LEFT), dfs(root.right, 0, RIGHT), curCount)

        return max(dfs(root.left, 0, LEFT), dfs(root.right, 0, RIGHT))