
# https://www.youtube.com/watch?v=lPmkKnvNPrw
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:


        points.sort()
        print(points)
        balloons = len(points)
        prevStart, prevEnd = points[0][0], points[0][1]
        
        for start,end in points[1:]:
            if start <= prevEnd:
                balloons -= 1
                prevStart = start
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
                prevStart = start

        return balloons




        