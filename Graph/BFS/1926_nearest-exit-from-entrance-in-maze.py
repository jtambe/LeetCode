# https://www.youtube.com/watch?v=aIyi8068si4
from typing import List, Deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        rows, cols = len(maze), len(maze[0])
        q = Deque()
        q.append((entrance[0], entrance[1]))

        def inbound(x:int, y:int) -> bool:
            if(x >= 0 and x < rows and y >= 0 and y < cols):
                return True

        directions = [(+1,0),(-1,0),(0,+1),(0,-1)]

        # Just like in the case of rotten oranges, we pull in the nearest nodes from starting position in q first
        for dx,dy in directions:
            x,y = q[0][0]+dx, q[0][1]+dy
            if inbound(x,y) and maze[x][y] == ".":
                q.append((x,y))
                print(q)

        startX, startY = q.popleft()
        maze[startX][startY] = "+" # It is important to convert the visited items as "+"

        time = 1
        while(q):
            for i in range(len(q)):
                cellX, cellY = q.popleft()
                for dx,dy in directions:
                    x,y = cellX+dx, cellY+dy
                    if not inbound(x,y):
                        return time
                    if inbound(x,y) and maze[x][y] == ".":
                        q.append((x,y))
                        maze[x][y] = "+" # It is important to convert the visited items as "+"
            time += 1

        return -1        