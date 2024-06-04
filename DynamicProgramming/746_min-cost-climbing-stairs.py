
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = cost
        i = len(dp)-3
        while(i >=0):
            dp[i] = min(dp[i]+dp[i+1], dp[i]+dp[i+2])
            i -= 1

        print(dp)
        return min(dp[0],dp[1])