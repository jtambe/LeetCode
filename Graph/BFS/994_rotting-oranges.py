from typing import List, Deque
# https://www.youtube.com/watch?v=y704fEOx0s0

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = Deque()

        def inbound(x:int, y:int) -> bool:
            if(x >= 0 and x < rows and y >= 0 and y < cols):
                return True

        # You cannot process 1st rotten orange region and then 2nd rotten orange region
        # You need to start off min = 1 for all rotten oranges at once
        # To achieve that, 
        # 1. Get all rotten oranges in a queue
        # 2. Then process all rotten oranges first in a loop
        # 3. Then process rest of the oranges as you add them in queue
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    fresh += 1
                if grid[x][y] == 2:
                    q.append([x,y])

        # use this for making code easily readable
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while(len(q) and fresh > 0):

            # We only need to process rotten oranges first
            # we can append, neighbors in queue but those are not processed until time is increased
            # If we use while(len(q) > 0), even 2nd layer of neighbors will get marked as rotten in same minute
            for i in range(len(q)): # This line makes sure, that you process all rotten oranges first. Thus not saying while(len(q) > 0)
                x,y = q.popleft()
                for dx, dy in directions:
                    row, col = x+dx, y+dy
                    if(inbound(row,col) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append([row,col])
                        fresh -= 1

            # for all the rotten oranges, nearby oranges will be rotten in minute 1
            # then 1 unit of time for all rotten oranges' all of the nearby neghbors
            # and so on and so on
            time += 1
        
        return time if fresh == 0 else -1