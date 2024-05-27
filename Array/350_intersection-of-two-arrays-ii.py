# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d1, d2 = {}, {}
        for x in nums1:
            if(x not in d1):
                d1[x] = 1
            else:
                d1[x] = d1[x]+1
        for x in nums2:
            if(x not in d2):
                d2[x] = 1
            else:
                d2[x] = d2[x]+1

        set1, set2 = set(nums1), set(nums2)
        intersect = set1.intersection(set2)

        ans = []
        for x in intersect:
            shows = min(d1[x],d2[x])
            for i in range(shows):
                ans.append(x)

        return ans
