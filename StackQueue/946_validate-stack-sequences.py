from typing import List, deque

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        # Create queue from popped
        q = deque(popped)
        # Simulation stack
        stack = []

        # Enter all elements from pushed into simulation stack
        for x in pushed:
            # Push each entry in simulation stack
            stack.append(x)
            # if pop can be performed, pop items
            while(any(q) and q[0] == stack[-1]):
                q.popleft()
                stack.pop()
                # after popping, if stack is empty, we must break from popping and add on stack
                if(not any(stack) and len(stack) == 0):
                    break

        # if all pop operations could be performed, we return that simulation can be performed
        if(any(q)):
            return False
        else:
            return True    



