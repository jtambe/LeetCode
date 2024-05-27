from typing import List
#https://leetcode.com/problems/find-the-highest-altitude/submissions/1264439387/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        maxAlt = 0
        for g in gain:
            alt = alt + g
            maxAlt = max(alt, maxAlt)

        return maxAlt