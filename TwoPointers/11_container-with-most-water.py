
from typing import List
#https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(height) -1
        while(left < right):
            minHeight = min(height[left], height[right])
            length = right - left
            maxArea = max(maxArea, minHeight * length)
            if height[left] < height[right]:
                left = left +1
            else:
                right = right -1

        return maxArea