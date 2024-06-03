class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        len1 = len(word1)
        len2 = len(word2)

        i = 0
        ans = ""
        while(i < max(len1, len2)):
            if i < len1:
                ans += word1[i]
            if i < len2:
                ans += word2[i]
            i += 1

        return ans
        