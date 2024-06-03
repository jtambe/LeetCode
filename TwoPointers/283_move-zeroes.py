
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return nums
        
        zeroCount = 0
        i = len(nums)-1
        while(i >= 0):

            if nums[i] == 0 and i < len(nums)-1:
                zeroCount += 1
                nums[i:] = nums[i+1:]
            i -= 1
        
        while(zeroCount >0):
            nums.append(0)
            zeroCount -= 1






        