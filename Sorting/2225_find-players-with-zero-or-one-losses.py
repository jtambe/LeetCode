
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        for x in matches:
            if(x[0] not in d):
                d[x[0]] = 0
            
            if(x[1] not in d):
                d[x[1]] = 1
            else:
                d[x[1]] = d[x[1]] + 1

        sortD = sorted(d.items(), key=lambda item:item[0])
        d = dict(sortD)

        ans = [[],[]]
        for k in d:
            if(d[k] == 0):
                ans[0].append(k)
            if(d[k] == 1):
                ans[1].append(k)

        return ans