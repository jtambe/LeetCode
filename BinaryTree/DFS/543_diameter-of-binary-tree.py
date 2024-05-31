# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        global dia
        dia = 0

        def dfs(root: TreeNode) -> int:
            
            # below leaf node, we return -1 as height
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            global dia
            # diameter = height of left subtree + right subtree + 2 edges from current node to left and right subtree
            # diameter at any leaf node = 2 + -1 (left subtree) + -1 (right subtree)
            dia = max(dia, 2 + left + right)

            # max height of left or right subtree + 1 = edge from current node to left or right subtree
            return 1 + max(left, right) 

        dfs(root)
        return dia
        
        