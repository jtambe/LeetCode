
#https://leetcode.com/problems/determine-if-two-strings-are-close/submissions/1264465170/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1) != len(word2)):
            return False

        d1, d2 = {}, {}
        for ch in word1:
            if ch not in d1:
                d1[ch] = 1
            else:
                d1[ch] = d1[ch] + 1
        for ch in word2:
            if ch not in d2:
                d2[ch] = 1
            else:
                d2[ch] = d2[ch] + 1 

        print(d1)
        print(d2)

        set1 = set([k for k in d1])
        set2 = set([k for k in d2])
        charDiff = set1.symmetric_difference(set2)
        if len(charDiff) > 0:
            return False

        # sortedD1 = sorted(d1.items(), key = lambda item:item[1])
        # sortedD2 = sorted(d2.items(), key = lambda item:item[1])
        # print(sortedD1)
        # print(sortedD2)

        # print(dict(sortedD1))
        # print(dict(sortedD2))

        freqD1 = {}
        freqD2 = {}
        for k in d1:
            if d1[k] not in freqD1:
                freqD1[d1[k]] = 1
            else:
                freqD1[d1[k]] = freqD1[d1[k]] + 1
        for k in d2:
            if d2[k] not in freqD2:
                freqD2[d2[k]] = 1
            else:
                freqD2[d2[k]] = freqD2[d2[k]] + 1
        print(freqD1)
        print(freqD2)

        #check the lengths of char frequency dictionaries are same
        if(len(freqD1) != len(freqD2)):
            return False

        #check if there are char frequecies that don't match in dicitonaries
        freqSet1 = set([k for k in freqD1])
        freqSet2 = set([k for k in freqD2])
        if(freqSet1.symmetric_difference(freqSet2)):
            return False


        # check if the number of chars with each frequecies are same in both dictionaries
        for k in freqD1:
            if(freqD1[k] != freqD2[k]):
                return False

        


        return True  