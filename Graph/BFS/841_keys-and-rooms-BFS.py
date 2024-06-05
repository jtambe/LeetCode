from typing import List, Deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        if len(rooms) == 1:
            return True

        if(len(rooms[0]) == 0):
            return False

        keys = set()
        keys.add(0)
        q = Deque()
        q.append(0)

        while q:
            room = q.popleft()
            for key in rooms[room]:
                if(key not in keys):
                    keys.add(key)
                    q.append(key)

        return True if len(keys) == len(rooms) else False
        