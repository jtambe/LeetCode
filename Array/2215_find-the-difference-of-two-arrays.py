from typing import List
#https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/1264443209/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        ans = []
        ans.append(set1.difference(set2))
        ans.append(set2.difference(set1))
        return ans