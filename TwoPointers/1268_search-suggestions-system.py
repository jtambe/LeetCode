# https://www.youtube.com/watch?v=D4T2N0yAr20
from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        ans = []
        products.sort()
        l,r = 0,len(products)-1

        for i in range(len(searchWord)):

            c = searchWord[i]

            while l <= r and (i >= len(products[l]) or products[l][i] != c):
                l += 1
            while l <= r and (i >= len(products[r]) or products[r][i] != c):
                r -= 1

            remainingWordsWindow = r -l + 1
            addWordsCount = min(3, remainingWordsWindow)
            ans.append(products[l: l + addWordsCount])

        return ans