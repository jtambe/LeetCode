from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] # pairs [temperature, index]
        ans = [0 for i in range(len(temperatures))] # Initialize all as 0s

        for idx, curT in enumerate(temperatures):
            while( any(stack)  and curT > stack[-1][0]): # if temperature is higher then pop until difference
                stackT, stackIdx = stack.pop()
                ans[stackIdx] = idx - stackIdx # ans for this position is difference
            
            # if stack is initially empty or if current temp is not greater than last one
            # keep stacking until we find higher temp than last one in stack
            stack.append([curT, idx]) 
        
        return ans