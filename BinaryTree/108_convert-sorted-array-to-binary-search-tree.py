# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.arrToTree(nums)
        return root
        
    def arrToTree(self, arr: List[int]) -> TreeNode:
        if len(arr) == 0:
            return 
        mid = len(arr)//2
        root = TreeNode(arr[mid])
        root.left = self.arrToTree(arr[:mid])
        root.right = self.arrToTree(arr[mid+1:])
        return root