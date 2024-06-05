from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        keys = set()
        keys.add(0)

        def dfs(room: int):
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    keys.add(key)
                    dfs(key)
            else:
                return


        for i in range(len(rooms)):
            if i not in visited and i in keys:
                dfs(i)

        return True if len(visited) == len(rooms) else False