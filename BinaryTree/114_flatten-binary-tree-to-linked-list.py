# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return []

        # Create a stack
        stack = []
        self.preorder(root, stack)

        # Maintain 2 variables for last and current
        last = stack.pop()
        last.left, last.right = None, None
        while(any(stack)):
            cur = stack.pop()
            cur.left = None
            cur.right = last
            last = cur

    # Function that pushes nodes on stack in pre-order fashion
    def preorder(self, root: TreeNode, stack: List[TreeNode]):
        if(root is None):
            return
        stack.append(root)
        self.preorder(root.left, stack)
        self.preorder(root.right, stack)