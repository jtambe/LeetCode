# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def preorderTraversal_Helper(root:  Optional[TreeNode], result: List[int]):
            if root is None:
                return
            result.append(root.val)
            preorderTraversal_Helper(root.left, result)
            preorderTraversal_Helper(root.right, result)
        
        result = []
        preorderTraversal_Helper(root, result)

        return result
