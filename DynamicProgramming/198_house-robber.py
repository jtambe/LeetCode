from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        # if there are only 2 houses or less, simply take the maximum of them
        if(len(nums) <=2):
            return max(nums)

        #create mm = MaximumMoney at each index
        mm = []
        mm.append(nums[0])
        mm.append(nums[1])
        i = 2
        while(i < len(nums)):
            # for each index, maximum money that can be robbed is maxmoney upto currentIndex-2 + money from currentIndex
            mm.append(max(mm[:i-2+1]) + nums[i])
            i = i+1

        return max(mm)
        