
from typing import List

# https://www.youtube.com/watch?v=HsGKI02yw6M

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        max_w = 0
        num_zeroes = 0
        n = len(nums)
        l = 0

        for r in range(n):
            if nums[r] == 0:
                num_zeroes += 1

            while(num_zeroes > k):
                if(nums[l] == 0):
                    num_zeroes -= 1
                l += 1

            w = r - l +1
            max_w = max(w, max_w)

        return max_w

        
            




        