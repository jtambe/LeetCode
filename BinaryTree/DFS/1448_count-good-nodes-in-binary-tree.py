from typing import math 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        global good_nodes_count
        good_nodes_count = 0
        maxVal = -(math.inf)

        def dfs(root: TreeNode, maxVal: int):
            
            global good_nodes_count
            if root is None:
                return
            
            if root.val >= maxVal:
                good_nodes_count += 1
                maxVal = max(maxVal, root.val)
            print(f"root.val:{root.val} maxVal:{maxVal} good_nodes_count:{good_nodes_count}")

            if root.left:
                dfs(root.left, maxVal)
            if root.right:
                dfs(root.right, maxVal)

        dfs(root, maxVal)
        return good_nodes_count
        