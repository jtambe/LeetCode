# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Youtube: https://www.youtube.com/shorts/tpIho2vhkho
        def isValid(node, left, right):
            if node is None:
                return True
            if not (left < node.val < right):
                return False
            return (
                isValid(node.left, left, node.val) and
                isValid(node.right, node.val, right)
            )

        return isValid(root, float("-inf"), float("inf"))


    """
    Following approach simply creates and checks in-order array increments
    """
    def isValidBST_extra_memory(self, root: Optional[TreeNode]) -> bool:
        bstArr = []
        self.get_inorder_array(root, bstArr)
        # print(bstArr)
        return self.is_arr_inorder(bstArr)
    
    def get_inorder_array(self, root: Optional[TreeNode], bstArr):
        if root is None:
            return
        else:
            self.get_inorder_array(root.left, bstArr)
            bstArr.append(root.val)
            self.get_inorder_array(root.right, bstArr)
    
    def is_arr_inorder(self, bstArr) -> bool:
        if len(bstArr) == 0:
            return True
        
        for i in range(1, len(bstArr)):
            if bstArr[i] <= bstArr[i-1]:
                return False

        return True
