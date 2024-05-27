# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None

        arr = self.listToArray(head)
        root = self.arrToTree(arr)
        return root

    def arrToTree(self, arr: List[int]) -> TreeNode:
        if len(arr) == 0:
            return 
        mid = len(arr)//2
        root = TreeNode(arr[mid])
        root.left = self.arrToTree(arr[:mid])
        root.right = self.arrToTree(arr[mid+1:])
        return root


    def listToArray(self, head: ListNode) -> List[int]:
        cur = head
        arr = []
        while(cur):
            arr.append(cur.val)
            cur = cur.next
        return arr
    