from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        # Edge case
        if(len(nums) < 3):
            return max(nums)

        # Do forward pass
        mm = []
        mm.append(nums[0])
        mm.append(nums[1])
        i = 2
        while(i < len(nums) - 1):
            s = max(mm[:i-1])
            mm.append(max(s, s + nums[i]))
            i += 1
        
        l = max(mm)

        # Do backward pass
        mm = []
        mm.append(nums[-1])
        mm.append(nums[-2])
        i = len(nums) - 3
        while(i >= 1):
            s = max(mm[:len(mm) - 1])
            mm.append(max(s, s + nums[i]))
            i -= 1
        
        r = max(mm)

        # Get max from both passes
        return max(l,r)