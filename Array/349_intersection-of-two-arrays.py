from typing import List

# https://leetcode.com/problems/intersection-of-two-arrays/submissions/1265275613/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return set1.intersection(set2)
        