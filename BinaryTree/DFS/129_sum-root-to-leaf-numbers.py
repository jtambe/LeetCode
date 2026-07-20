# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        allNums = []
        curStack = []

        def get_number(arr: List[int]) -> int:
            """
            convert array of numbers to a single number
            """
            k = 1
            n = len(arr)
            num = 0
            for i in range(n-1, -1, -1):
                num = num + arr[i] * k
                k *= 10
            return num


        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            if node.left is None and node.right is None:
                # when leaf node is reached, create number for summation
                curStack.append(node.val)
                curNum = get_number(curStack)
                allNums.append(curNum)
                curStack.pop() # pop this leaf node from stack
                return 

            curStack.append(node.val)
            dfs(node.left)
            dfs(node.right)
            curStack.pop() # don't forget to pop intermediate nodes when moving up the stack
        

        dfs(root)
        print(f"allNums:{allNums}")
        return sum(allNums)
