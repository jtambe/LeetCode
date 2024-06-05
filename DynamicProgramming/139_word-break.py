# https://www.youtube.com/watch?v=Sx9NNgInc3A&t=4s

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for i in range(len(s)+1)]
        dp[-1] = True
        wordSet = set(wordDict)
        i = len(s)-1

        while(i >= 0):
            for word in wordSet:
                if i+len(word) <= len(s) and s[i : i+len(word)] in wordSet:
                    dp[i] = dp[i+len(word)]
                    if dp[i] == True:
                        break
            i -= 1

        return dp[0]