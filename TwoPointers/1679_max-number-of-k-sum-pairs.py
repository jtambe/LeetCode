
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations, left, right = 0, 0, len(nums) - 1
        nums.sort()
        #print(nums)

        while(left < right):
            if(nums[left] + nums[right] == k):
                operations = operations + 1
                left = left + 1
                right = right - 1
            elif(nums[left] + nums[right] < k):
                left = left + 1
            else:
                right = right - 1


        return operations