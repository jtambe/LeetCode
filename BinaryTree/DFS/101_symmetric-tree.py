# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Should be called isMirror instead
        """

        def isMirror(left, right):
            if left is None and right is None:
                return True
            if (left and not right) or (right and not left) or (left.val != right.val):
                return False
            
            
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root, root)
