
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1

        set1 = set([])
        for k in d:
            if d[k] in set1:
                return False
            else:
                set1.add(d[k])

        return True