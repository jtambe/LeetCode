# https://www.youtube.com/watch?v=hPlI-M5Iu6A

class Solution:
    def myPow(self, x: float, n: int) -> float:

        is_neg = n < 0
        self.memo = {}
        n = abs(n)
        result = self.pow_dp(x, n)

        return 1/result if is_neg else result

    def pow_dp(self, x: float, n: int) -> float:

        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 1
        if n == 1:
            return x

        self.memo[n] = self.pow_dp(x, n//2) * self.pow_dp(x, n//2) * (x if (n%2 != 0) else 1)

        return self.memo[n]



# without using extra memory and using @cache by python
# solution 2
from typing import cache
class Solution2:
    def myPow(self, x: float, n: int) -> float:

        is_neg = n < 0
        n = abs(n)
        result = self.pow_dp(x, n)

        return 1/result if is_neg else result

    @cache
    def pow_dp(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        if n == 1:
            return x

        return self.pow_dp(x, n//2) * self.pow_dp(x, n//2) * (x if (n%2 != 0) else 1)
        