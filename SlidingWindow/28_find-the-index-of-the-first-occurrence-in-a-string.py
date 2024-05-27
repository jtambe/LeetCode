#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        needleLength = len(needle)
        haystackLength = len(haystack)

        if(needleLength > haystackLength):
            return -1
        if(needleLength == haystackLength and needle == haystack):
            return 0

        index = 0
        while(index <= haystackLength - needleLength):
            print(haystack[index : index + needleLength])
            if(haystack[index : index + needleLength] == needle):
                return index
            else:
                index = index + 1
        

        return -1