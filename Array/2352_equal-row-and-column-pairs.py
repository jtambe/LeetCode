from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        
        colStrings = []
        rowStrings = []

        for y in range(cols):
            colString = ""
            for x in range(rows):
                colString += str(grid[x][y]) + "-"
            colStrings.append(colString)

        for x in range(rows):
            rowString = ""
            for y in range(cols):
                rowString += str(grid[x][y]) + "-"
            rowStrings.append(rowString)

        print(rowStrings)
        print(colStrings)

        count = 0
        for idx, x in enumerate(rowStrings):
            for idy, y in enumerate(colStrings):
                if x == y:
                    count += 1

        return count        
            

        