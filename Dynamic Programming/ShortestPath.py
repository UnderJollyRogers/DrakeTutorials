import heapq
from collections import defaultdict

def label_correcting_algorithm(graph, start, end):
    # Distance from start node to all other nodes. Default to a very high value.
    distances = defaultdict(lambda: float('inf'))
    # Parent node in the path
    parents = {}
    # Nodes to explore
    open_set = []
    
    # Initialize the start node
    distances[start] = 0
    heapq.heappush(open_set, (0, start))
    
    while open_set:
        current_distance, current_node = heapq.heappop(open_set)
        
        # Early exit if we reach the end node
        if current_node == end:
            break
        
        # Explore each adjacent node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heapq.heappush(open_set, (distance, neighbor))
    
    # Reconstruct the path from end to start
    path = []
    step = end
    while step != start:
        path.append(step)
        step = parents[step]
    path.append(start)
    path.reverse()
    
    return path, distances[end]

# Find the shortest path from 'A' to 'D'
path, cost = label_correcting_algorithm(graph, 'A', 'D')
print("Shortest path:", path)
print("Total cost:", cost)
