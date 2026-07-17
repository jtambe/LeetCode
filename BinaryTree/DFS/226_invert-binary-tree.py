# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import copy

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if node is None:
                return
            
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root





    def invertTree_deepcopy(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        invertRoot = copy.deepcopy(root)
        # print(f"root: {hex(id(root))}")
        # print(f"invertRoot: {hex(id(invertRoot))}")

        def dfs(og, new):
            if og is None:
                return
            
            new.left = copy.deepcopy(og.right)
            new.right = copy.deepcopy(og.left)
            dfs(og.left, new.right)
            dfs(og.right, new.left)


        dfs(root, invertRoot)
        return invertRoot
        
