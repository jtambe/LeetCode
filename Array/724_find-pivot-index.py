
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        for idx, i in enumerate(nums):
            if leftSum == totalSum - leftSum - i:
                return idx
            leftSum = leftSum + i

        return -1