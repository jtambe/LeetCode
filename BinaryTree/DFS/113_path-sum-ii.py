# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []
        cur = []
        self.helper(root, 0, targetSum, cur, ans)
        return ans

    def helper(self, root: TreeNode, currentSum: int, targetSum:int, curList: List[int], ans:List[List[int]]):
            # if root is None:
            #     return
            curList.append(root.val)
            currentSum += root.val
            #print(f"{root.val} sum:{currentSum} list:{curList} ans:{ans}")
            if(root.left is None and root.right is None and targetSum == currentSum):
                lst= curList.copy() # it is very important to create a copy and push in the ans otherwise that list gets overwritten
                ans.append(lst)
            else:
                if root.left:
                    self.helper(root.left, currentSum, targetSum, curList, ans)
                    curList.pop()
                if root.right:
                    self.helper(root.right, currentSum, targetSum, curList, ans)
                    curList.pop()
            
        