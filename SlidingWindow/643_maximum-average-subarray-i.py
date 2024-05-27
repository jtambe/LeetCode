from typing import List
from typing import inf

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = float(-inf)
        left, right, sum = 0, 0, 0

        #first round of k elements
        while(right < k):
            sum = sum + nums[right]
            right = right + 1
        avg = sum / k
        right = right - 1
        maxAvg = max(maxAvg, avg)
        
        while(right < len(nums) - 1):
            sum = sum - nums[left]
            print(sum)
            left = left + 1
            right = right + 1
            sum = sum + nums[right]
            avg = sum /k
            maxAvg = max(maxAvg, avg)

        return maxAvg