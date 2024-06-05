from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        # #Solution 1
        # for i in range(n+1):
        #     ans.append(bin(i).count('1'))

        # Solution 2
        for i in range(n+1):
            count = 0
            num = i
            while(num > 0):
                if num & 1:
                    count += 1
                num = num >> 1
            ans.append(count)

        return ans