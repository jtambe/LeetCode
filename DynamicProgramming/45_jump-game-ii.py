from typing import List, math
#https://leetcode.com/problems/jump-game-ii/submissions/1265168369/

class Solution:
    def jump(self, nums: List[int]) -> int:

        # build dp array
        infinity = math.inf
        minsteps = [infinity for i in range(len(nums))]


        # add values from back
        minsteps[len(nums) - 1] = 0

        # Go in reverse to find min jumps at each step
        i = len(nums) - 2
        while(i >= 0):
            # if you cannot move from this position, then mark it as inf
            if(nums[i] == 0):
                minsteps[i] = math.inf
            
            # from current position, find out what positions can you go to (i + nums[i])
            # find a position which has min steps to get to goal
            # add one jump to that position 
            minstep = math.inf
            for x in range(1,nums[i] + 1): # You can take nums[i] jumps
                if(i+x < len(minsteps)): # Cannot cross array index
                    minstep = min(minstep, minsteps[i+x])
            minsteps[i] = minstep + 1 # add min jumps + 1 (current position jump)

            i = i -1
        return minsteps[0]