from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        # Neetcode
        # https://www.youtube.com/watch?v=LN7KjRszjk4
        

        for idx, num in enumerate(asteroids):
            #print(f"stack:{stack} num:{num}")
            while(any(stack) and (stack[-1] > 0 and num < 0)):
                diff = num + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    num = 0
                else:
                    num = 0
                    stack.pop()

            if(num != 0):
                stack.append(num)
                    
            

        return stack



        
        

        