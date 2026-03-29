"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 
Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l, r = 0, n

        while l < r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if mid > 0 and nums[mid-1] < target:
                    return mid
                if mid == 0:
                    return 0
                r = mid
            else:
                if mid+1 < n and nums[mid+1] > target:
                    return mid + 1
                if mid == n-1:
                    return n
                l = mid + 1


        