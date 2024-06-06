# https://www.youtube.com/watch?v=tmJnNdP__0c
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        # find pivot
        while(l < r):
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid

        pivot = l
        print(f"pivot:{pivot} nums[pivot]:{nums[pivot]}")

        l, r = 0, len(nums)-1
        while(l <= r):
            mid = (l+r)//2
            mid2 = (mid + pivot) % len(nums)

            print(f"mid = {l}+{r} % 2 = {mid}")
            print(f"mid2 = {mid}+{pivot} % {len(nums)} = {mid2}")
            print(f"nums[mid2]: {nums[mid2]}")

            if target == nums[mid2]:
                return mid2
            if nums[mid2] < target:
                l = mid+1
            if nums[mid2] > target:
                r = mid-1


        return -1