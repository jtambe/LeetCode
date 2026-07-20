# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        inorder = []
        def inorder_dfs(node: Optional[TreeNode]):
            if node is None:
                return
            inorder_dfs(node.left)
            inorder.append(node.val)
            inorder_dfs(node.right)
        
        inorder_dfs(root)

        return inorder
