
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        a = []
        cur = head
        while(cur):
            a.append(cur.val)
            cur = cur.next
        
        if len(a) == 2:
            return sum(a)

        maxSum = 0
        l,r = 0,len(a)-1
        while(l < r):
            maxSum = max(a[l]+a[r], maxSum)
            l += 1
            r -= 1

        return maxSum



class Solution2:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = self.get_count(head)
        reversed_head = self.get_reverse_list_head(head, n)
        i = 0
        max_sum = 0
        cur, rev_cur = head, reversed_head
        while(i < n//2):
            max_sum = max(max_sum , cur.val + rev_cur.val)
            cur, rev_cur = cur.next, rev_cur.next
            i += 1
        return max_sum

    def get_reverse_list_head(self, head: Optional[ListNode], n:int) -> ListNode:
        i = 0
        cur = head
        while(i < n//2):
            cur = cur.next
            i += 1

        prev = None
        while(cur):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def get_count(self, head: Optional[ListNode]) -> int:
        count = 0
        cur = head
        while(cur):
            cur = cur.next
            count += 1
        return count

