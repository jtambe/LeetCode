# https://www.youtube.com/watch?v=nONCGxWoUfM

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # def mySortFunc(item: List[int]):
        #     return item[0]
        # ordered = sorted(intervals, key=mySortFunc)

        intervals.sort()
        removeCount = 0
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                prevEnd = min(prevEnd, end)
                removeCount += 1

        return removeCount




        



        