"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
If there exists a solution, it is guaranteed to be unique.

 

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 

Constraints:
n == gas.length == cost.length
1 <= n <= 10^5
0 <= gas[i], cost[i] <= 10^4
The input is generated such that the answer is unique.
"""

from typing import List

class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # if we don't have enough fuel, we cannot finish
        if sum(gas) < sum(cost):
            return -1

        start = 0 # starting index
        cur_gas = 0 # previous gas value before journey begins. Think of it like prev head when reversing LinkedList

        for i in range(len(gas)):
            cur_gas = cur_gas + gas[i] - cost[i]

            # we know that 
            # 1. At least 1 solution exists.
            # 2. Every problem 1 unique solution. 
            # So there is only 1 starting index and all throughout the iteration, cur_gas should not be less than 0
            # Which means, if it ever becomes < 0, we simply move the start position of journey
            if cur_gas < 0:
                start = i+1
                cur_gas = 0

        return start
                            



    def canCompleteCircuit_timeout(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        if n == 1:
            if gas[0] >= cost[0]:
                return 0
            else:
                return -1

        max_diff_index = 0
        max_diff = float('-inf')
        for i in range(n):
            if gas[i] - cost[i] > max_diff:
                max_diff_index = i
        
        index = max_diff_index
        while True:
            cur_total_gas = 0
            i = index
            if gas[i] - cost[i] >= 0:
                cur_total_gas = gas[i] 
                while i < n and i >= 0:
                    cur_total_gas -= cost[i]
                    i = (i+1) % n
                    cur_total_gas += gas[i]
                    if i == index and cur_total_gas - cost[i] >= 0:
                        return index
                    if cur_total_gas - cost[i] < 0:
                        break
            
            index = (index+1) % n
            if index == max_diff_index:
                break
                    
        return -1
                        



