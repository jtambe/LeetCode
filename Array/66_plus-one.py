class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 0
        n = len(digits)
        for i in range(n-1,-1,-1):
            newDigit = digits[i] + carry + (1 if i == n-1 else 0)
            if newDigit > 9:
                carry = 1
            else:
                carry = 0
            digits[i] = newDigit % 10
        
        if carry == 1:
            # digits[1:] = digits[0:len(digits)]
            # digits[0] = 1
            digits = [1] + digits

        return digits

        
