class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        islands_count = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        def inbound(x:int, y:int) -> bool:
            if(x >= 0 and x < rows and y >= 0 and y < cols):
                return True

        def dfs(i: int, j: int):
            for dx, dy in directions:
                row, col = i+dx, j+dy
                location = str(row) + "-" + str(col)
                if location not in visited and inbound(row,col):
                    visited.add(location)
                    if grid[row][col] == "1":
                        dfs(row, col)



        for row in range(rows):
            for col in range(cols):
                location = str(row) + "-" + str(col)
                if location not in visited:
                    visited.add(location)
                    if grid[row][col] == "1":
                        islands_count += 1
                        dfs(row, col)


        return islands_count


    


        
