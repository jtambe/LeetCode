"""
Given the head of a linked list, return the list after sorting it in ascending order.
Youtube: https://www.youtube.com/shorts/USyuCNeCxKU

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:
Input: head = []
Output: []
 

Constraints:
The number of nodes in the list is in the range [0, 5 * 10^4].
-10^5 <= Node.val <= 10^5

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""

#Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.divide(head)
        
    def divide(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base condition
        if not head or not head.next:
            return head

        # two pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # divide the list
        mid = slow.next
        slow.next = None

        # divide furhter recursively until just 1 item in left and right
        left = self.divide(head)
        right = self.divide(mid)

        # merge left and right lists
        return self.merge(left, right)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return dummy.next




