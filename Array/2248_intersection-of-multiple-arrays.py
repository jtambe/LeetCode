
from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        intersect = set(nums[0])
        for i in range(1, len(nums)):
            curset = set(nums[i])
            intersect = intersect.intersection(curset)

        ans = list(intersect)
        ans.sort()
        return ans

        