class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_string = ''.join([x for x in s.lower() if x.isalnum()])
        i, j = 0, len(clean_string) -1

        while(i < j):
            if clean_string[i] == clean_string[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True
