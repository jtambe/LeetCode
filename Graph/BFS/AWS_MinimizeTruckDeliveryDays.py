"""

A new e-commerce website is launched, they have warehouses setup in a couple of locations across the world. (mxn world representation).
Currently they have only procured trucks for delivery, which travel only to adjacent countries by road (vertical and horizontal). 
There are no roads on water. An average truck takes 20 days to travel between two countries. 
Find the least number of days taken to deliver to the entire world, if at all.

Input - worldMap : 2D Array
* C : country
  - O - No warehouse
  - X - Has warehouse
* W - water

For Reference - World Map
[C W C W C C C
 W C W C C W C
 W W C C W W C
 W C C C W W C
 C C W C W C C]

 
[X1 W O2]
1-> 0 days
2 -> 20 days (1-> 2 : 20 )
 


Actual Input -
[X O X W O X O
 W O W O X W O
 W W N O W W O
 W O O O W W O
 X X W O W O X]


 Interpretation:
 X are locations that have trucks
 O are location that don't have trucks
 W is water and trucks can't go over water
 Starting from all X can trucks deliver to all O locations?
 If they can, how many days will it take? 
 Moving to O location from X or from O takes 20 days
""" 


from typing import List, Deque

class Solution:
    def deliveryCost(self, map: List[List[str]]) -> int:
        
        q = Deque()
        rows, cols = len(map), len(map[0])
        days = 0
        countCountries = 0
        dirs = [(0,+1), (0,-1),(+1,0),(-1,0)]
        
        def inbound(x:int, y:int) -> bool:
            if x >= 0 and x < rows and y >= 0 and y < cols:
                return True
            else:
                return False
        
        # starting positions for BFS
        for x in range(rows):
            for y in range(cols):
                if map[x][y] == "X":
                    q.append((x,y))
                    countCountries += 1
                if map[x][y] == "O":
                    countCountries += 1
                    
        
        visited = set()
        while(q):
            for i in range(len(q)):
                cellX, cellY = q.popleft()
                visited.add((cellX, cellY))
                countCountries -= 1
                for dx,dy in dirs:
                    x,y = cellX+dx, cellY+dy
                    if inbound(x,y) and map[x][y] == "O":
                        if (x,y) not in visited:
                            visited.add((cellX, cellY))
                            q.append((x,y))
                            countCountries -= 1
            if len(q) > 0:                            
                days += 20
                    
        
        return days if countCountries == 0 else -1
    

def createMap(mapstr: str) -> List[List[str]]:
    map = []
    lines = mapstr.split("\n")
    for line in lines:
        chars = line.split(" ")
        del chars[-1]
        del chars[0]
        map.append(chars)
    return map
    
mapstr = "X O X W O X O \n W O W O X W O \n W W N O W W O \n W O O O W W O \n X X W O W O X"
map = createMap(mapstr)
print(map)

sln = Solution()
ans = sln.deliveryCost(mapstr)
print(ans)


    