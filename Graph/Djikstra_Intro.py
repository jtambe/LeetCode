"""
Intro to Djikstra's algorithm using Google AI
"""
import heapq

def dijkstra(graph, start):
    # Initialize distances to infinity and start node to 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue stores (distance, node)
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we found a longer path than already recorded, skip
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If new path is shorter, update and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# Example graph: { 'Node': { 'Neighbor': weight } }
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijkstra(graph, 'A'))


"""
{'A': 0, 'B': 1, 'C': 3, 'D': 4}
"""
