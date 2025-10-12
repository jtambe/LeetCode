class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g = sorted(g)
        s = sorted(s)

        # print(f"s: {s}")
        # print(f"g: {g}")

        i, j, count = 0, 0, 0
        while(i < len(s) and s[i] < g[0]):
            i += 1

        while(i < len(s) and j < len(g)):
            if (s[i] >= g[j]):
                count += 1
                j += 1
            i += 1


        return count
        
