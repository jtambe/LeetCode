"""
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.


Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        This is essentially brute force approach after sorting
        """
        nums.sort()
        closest_sum = sum(nums[0:4])
        closest_diff = abs(target - closest_sum)
        n = len(nums)

        for i in range(n):

            l, r =  i+1, n-1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                cur_diff = abs(target - cur_sum)
                
                if cur_diff == 0:
                    return cur_sum
                else:
                    if cur_diff < closest_diff:
                        closest_diff = cur_diff
                        closest_sum = cur_sum
                
                l, r = l+1, r-1

        return closest_sum
            


        