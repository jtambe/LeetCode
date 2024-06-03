class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        minStr = str1 if len(str1)<len(str2) else str2

        i = len(minStr)-1
        while(i >= 0):
            print(minStr[:i+1])
            if self.isDivisor(str1, minStr[:i+1]) and self.isDivisor(str2, minStr[:i+1]):
                return minStr[:i+1]
            i -= 1

        return ""

    def isDivisor(self, word: str, dividend: str) -> bool:
        multiple = len(word)//len(dividend)
        checker = ""
        for i in range(multiple):
            checker += dividend
        
        return True if checker == word else False

        