from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        thor = 0
        for x in nums:
            thor = thor ^ x

        return thor
        