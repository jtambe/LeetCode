# https://www.youtube.com/watch?v=EgI5nU9etnU&t=686s
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        d = {}
        for item in prerequisites:
            if item[0] in d:
                d[item[0]].add(item[1])
            else:
                dset = set()
                dset.add(item[1])
                d[item[0]] = dset
        for i in range(numCourses):
            if i not in d:
                d[i] = set()
        #print(d)
        
        def hasCircularDependency(i: int, visited: set) -> bool:
            if i in visited:
                return True
            if not d[i]:
                return False
            visited.add(i)
            for x in d[i]:
                if hasCircularDependency(x, visited): 
                    return True
            visited.remove(i) # this node is now covered
            d[i] = set() # all of this node's dependencies are also covered
            
                         

        for i in range(numCourses):
            visited = set()
            circular = hasCircularDependency(i, visited)
            if circular:
                return False

        return True