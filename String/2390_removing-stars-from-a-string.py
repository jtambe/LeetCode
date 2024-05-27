class Solution:
    def removeStars(self, s: str) -> str:
        
        i = 0
        stack = []
        while(i < len(s)):
            stack.append(s[i])
            if(s[i] == "*"):
                stack.pop()
                stack.pop()
            i += 1

        res = "".join(stack)
        return res
        