from typing import List
# https://www.youtube.com/watch?v=S5UUvCTM0V4

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        totalCities = len(isConnected)

        def dfs(city):
            visited.add(city)
            for neighbor in range(totalCities):
                if(isConnected[city][neighbor] == 1 and neighbor not in  visited):
                    dfs(neighbor)

        visited = set()
        provinces = 0
        # Every city that is not already visited will start new province
        # In the DFS, add city's neighbors in visited, so they are not considered again
        for city in range(totalCities):
            if(city not in visited):
                provinces += 1
                dfs(city)

        return provinces
        