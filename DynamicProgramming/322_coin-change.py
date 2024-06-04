
from typing import List, math, cache

# https://www.youtube.com/watch?v=xxrv-uJdV8Y

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        @cache
        def dp(n: int):
            res = math.inf
            if n == 0:
                return 0

            for c in coins:
                if c <= n:
                    res = min(res, dp(n-c) +1)
            return res

        res = dp(amount)
        
        return res if res != math.inf else -1