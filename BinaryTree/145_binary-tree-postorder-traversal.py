# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def postorderTraversal_Helper(root:  Optional[TreeNode], result: List[int]):
            if root is None:
                return
            postorderTraversal_Helper(root.left, result)
            postorderTraversal_Helper(root.right, result)
            result.append(root.val)
        
        result = []
        postorderTraversal_Helper(root, result)
        
        return result
