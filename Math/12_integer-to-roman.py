
# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""

        while(num >= 1000):
            num = num - 1000
            ans = ans + "M"

        if(num >= 900):
            num = num - 900
            ans = ans + "CM"
        
        while(num >= 500):
            num = num - 500
            ans = ans + "D"

        if(num >= 400):
            num = num - 400
            ans = ans + "CD"

        while(num >= 100):
            num = num - 100
            ans = ans + "C"
        
        if(num >= 90):
            num = num - 90
            ans = ans + "XC"
        
        while(num >= 50):
            num = num - 50
            ans = ans + "L"

        if(num >= 40):
            num = num - 40
            ans = ans + "XL"
        
        while(num >= 10):
            num = num - 10
            ans = ans + "X"

        if(num >= 9):
            num = num - 9
            ans = ans + "IX"

        while(num >= 5):
            num = num - 5
            ans = ans + "V"

        if(num >= 4):
            num = num - 4
            ans = ans + "IV"

        while(num >= 1):
            num = num - 1
            ans = ans + "I"

        return ans
    