
from typing import List
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if( len(nums) == 1):
            return 1

        left, right, curNum = 0, 0, nums[0]
        while(right < len(nums) - 1):
            while(right < len(nums) -1 and nums[right] == curNum):
                right = right + 1
            if(nums[right] != nums[left]):
                left = left + 1
                print(f"left:{left} right:{right}")
                nums[left] = nums[right]
                curNum = nums[right]

        print(left+1)
        return left+1
