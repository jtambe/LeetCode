"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

 

Example 1:
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
 

Constraints:
1 <= nums.length <= 10^4
-10^7 <= nums[i] <= 10^7
0 <= k <= 10^7
"""

from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        Time complexity = O(nlogn)
            1. sorting is most expensive
            2. (n * (logn)) < n times (logn) binary search for all n items in array
        Space complexity = O(1)
            1. No extra array or set or dictionary used
        """

        nums.sort()
        n = len(nums)
        total_pairs = 0

        def binarySearch(item: int, sorted_arr: List[int]):
            l, r = 0, len(sorted_arr)
            while(l < r):
                mid = (l+r)//2
                if item == sorted_arr[mid]:
                    return True
                elif item < sorted_arr[mid]:
                    r = mid
                elif item > sorted_arr[mid]:
                    l = mid + 1

            return False

        for i in range(n):
            # get current item
            cur = nums[i]
            # do not repeat current item
            if i-1 >= 0  and nums[i] == nums[i-1]:
                continue

            # find 2 numbers we would need to match the condition
            needed_1 = cur - k
            needed_2 = cur + k
           
            # binary search those 2 numbers
            if binarySearch(needed_1, nums[i+1: n]):
                total_pairs += 1
            if needed_1!= needed_2 and binarySearch(needed_2, nums[i+1: n]):
                total_pairs += 1

        return total_pairs