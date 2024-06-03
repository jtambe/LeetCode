from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        max_w = 0
        k = 1
        flipped = 0
        l = 0

        for r in range(len(nums)):

            if nums[r] == 0:
                flipped += 1

            while flipped > k:
                if nums[l] == 0:
                    flipped -= 1
                l += 1

            w = r - l +1
            max_w = max(max_w, w)

        return max_w -1
    


s = Solution()
nums = [1,1,0,1]
print(s.longestSubarray(nums))
nums = [0,1,1,1,0,1,1,0,1]
print(s.longestSubarray(nums))
nums = [1,1,1]
print(s.longestSubarray(nums))
nums = [0,0,0]
print(s.longestSubarray(nums))