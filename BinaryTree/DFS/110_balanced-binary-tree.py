# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from functools import cache
from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        @cache
        def subtree_height(node):
            if node is None:
                return 0
            left = 1 + subtree_height(node.left)
            right = 1 + subtree_height(node.right)
            return max(left,right)

        def check_all_nodes(node):
            if node is None:
                return True
            if abs(subtree_height(node.left) - subtree_height(node.right)) > 1:
                return False
            return check_all_nodes(node.left) and check_all_nodes(node.right)

        return check_all_nodes(root)
    

    def isBalanced_YouTube(self, root: Optional[TreeNode]) -> bool:
        """
        https://www.youtube.com/shorts/gGvFnycOtxs
        """
        balanced = [True]

        def height(node):
            if not node:
                return 0
                
            left = height(node.left)
            right = height(node.right)

            if abs(left - right) > 1:
                balanced[0] = False

            return 1 + max(left, right)
        

        height(root)
        return balanced[0]
    

    
    def isBalanced_Copilot(self, root: Optional[TreeNode]) -> bool:
        """
        Copilot solution
        """

        def dfs(node):
            if node is None:
                return (True, 0)  # (is_balanced, height)
            
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)
            
            is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return (is_balanced, height)

        return dfs(root)[0]

        
