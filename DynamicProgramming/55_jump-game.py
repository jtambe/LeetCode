from typing import List
# https://leetcode.com/problems/jump-game/submissions/1265182872/

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        jump = []
        for i in range(len(nums)):
            jump.append(False)
        
        #print(jump)

        #jump = [False for i in range(len(nums))]

        jump[len(jump) - 1] = True
        i = len(jump) - 2
        while(i >= 0):
            if(nums[i] == 0):
                jump[i] = False
            
            for x in range(nums[i]+1):
                possible = False
                if(i+x < len(jump) and jump[i+x] == True):
                    possible = True
                    break
            
            jump[i] = possible
            i = i-1

        return jump[0]
        