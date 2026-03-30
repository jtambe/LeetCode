"""
https://leetcode.com/problems/minimum-height-trees/description/
Algo explained by 
1. NeetCode: https://www.youtube.com/watch?v=wQGQnyv_9hI
2. https://www.youtube.com/watch?v=1ZDg3jk7dUE

A tree is an undirected graph in which any two vertices are connected by exactly one path. 
In other words, any connected graph without simple cycles is a tree.
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. 
When you select a node x as the root, the result tree has height h. 
Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]


Constraints:
1 <= n <= 2 * 10^4
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
"""

from typing import List
from typing import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n > 0 and n < 3:
            return [x for x in range(n)]
        
        edges_map = {}
        edge_count = {}
        def addEdgesInMap(node1, node2):
            if node1 in edges_map:
                edges_map[node1].append(node2)
                edge_count[node1] += 1
            else:
                edges_map[node1] = [node2]
                edge_count[node1] = 1
        
        for item in edges:
            addEdgesInMap(item[0], item[1])
            addEdgesInMap(item[1], item[0])

        leaves = deque()
        for k,v in edge_count.items():
            if v == 1:
                leaves.append(k)

        while leaves:
            # do this until there are only 2 or less leaves left, because there can be at most 2 MHTs
            if n <= 2:
                return list(leaves)
            # cut down all leaves at current level
            # add new leaves after removing edges by reducing edge count
            for i in range(len(leaves)):
                leaf = leaves.popleft()
                # leaf node is essentially out of tree and will not make it to MHT root
                n -= 1
                for neighbor in edges_map[leaf]:
                    edge_count[neighbor] -= 1
                    if edge_count[neighbor] == 1:
                        leaves.append(neighbor)










    def findMinHeightTrees_BFS(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        This approach logically works but times out on large dataset (test case 65)
        """

        # if n == 1:
        #     return [0]
        # if n == 2:
        #     return [0,1]
        if n > 0 and n < 3:
            return [x for x in range(n)]

        
        edges_map = {}
        def addEdgesInMap(node1, node2):
            if node1 in edges_map:
                edges_map[node1].append(node2)
            else:
                edges_map[node1] = [node2]
        for item in edges:
            addEdgesInMap(item[0], item[1])
            addEdgesInMap(item[1], item[0])
        # print(f"edges_map:{edges_map}")

        height_root_map = {}
        def getHeightRootMap(root):
            # print(f"######################################################")
            # print(f"root:{root}")
            visited = set()
            visited.add(root)
            q = deque()
            q.append(root)
            cur_height = 0
            while len(q) > 0:
                level_q = deque()
                while len(q) > 0:
                    node = q.popleft()
                    for cur_node in edges_map[node]:                    
                        if cur_node not in visited:
                            visited.add(cur_node)
                            level_q.append(cur_node)
                cur_height += 1
                # print(f"level_q:{level_q} at height:{cur_height}")                    
                height_root_map[root] = cur_height                
                q.extend(level_q)
                # print(f"q: {q}")

        for i in range(n):
            getHeightRootMap(i)

        # print(f"height_root_map:{height_root_map}")

        min_height = min(height_root_map.values())
        # print(f"min_height:{min_height}")
        
        min_height_roots = []
        for k,v in height_root_map.items():
            if v == min_height:
                min_height_roots.append(k)

        return min_height_roots
        