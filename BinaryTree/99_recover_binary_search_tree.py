# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# algorithm from you tube to identify first and second incorrect nodes when inorder traversal is applied
# https://www.youtube.com/watch?v=VxyAPV9nsCw

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        firstIncorrectNode = None
        secondIncorrectNode = None
        cur = None
        prev = None

        def inorder(root: Optional[TreeNode]):
            # very important use of nonlocal variables here
            nonlocal firstIncorrectNode, secondIncorrectNode, cur, prev 
            if root is None:
                return
            inorder(root.left)
            cur = root
            if prev and not firstIncorrectNode and cur.val < prev.val:
                firstIncorrectNode = prev
            if prev and firstIncorrectNode and cur.val < prev.val:
                secondIncorrectNode = cur
            prev = cur
            inorder(root.right)

        def swap(a:TreeNode, b:TreeNode):
           a.val, b.val = b.val, a.val

        # find 2 incorrect nodes during inorder traversal
        inorder(root)
        print(f"firstIncorrectNode: {firstIncorrectNode.val}")
        print(f"secondIncorrectNode: {secondIncorrectNode.val}")
        # only swap the values inside tree nodes. you don't need to swap left and right children pointers in the tree
        swap(firstIncorrectNode, secondIncorrectNode)
