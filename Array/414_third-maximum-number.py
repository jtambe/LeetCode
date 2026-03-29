"""
Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.
 

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
 

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
Follow up: Can you find an O(n) solution?
"""

from typing import List


import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)

        top_items = sorted(nums[:3])

        def rearrange(num: int):
            if num > top_items[2]:
                top_items[0], top_items[1], top_items[2] = top_items[1], top_items[2], num
            elif num > top_items[1] and num < top_items[2]:
                top_items[0], top_items[1] = top_items[1], num
            elif num > top_items[0] and num < top_items[1]:
                top_items[0] = num

        for i in range(3, len(nums)):
            rearrange(nums[i])

        return top_items[0]



    def thirdMax_solution2(self, nums: List[int]) -> int:

        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)

        # maxheap in python is implemented as minheap with negative values
        nums = [num * -1 for num in nums]
        heapq.heapify(nums)
        k = 3
        while k > 0:
            current = heapq.heappop(nums)
            k -= 1

        return current * -1