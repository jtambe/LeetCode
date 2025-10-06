# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        resultString: str = ""
        resultArray: List[str] = []

        self.inorder(root, resultString, resultArray)
        return resultArray

    
    # Build a string by doing in order traversal in recursion    
    def inorder(self, root: Optional[TreeNode], resultString:str, resultArray:List[str]):
            if root is None:
                return
            
            resultString = resultString + str(root.val) + "->"
            if root.left is None and root.right is None:
                resultArray.append(resultString.removesuffix("->"))
            
            self.inorder(root.left, resultString, resultArray )
            self.inorder(root.right, resultString, resultArray)

        




        
