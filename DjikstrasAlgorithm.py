import heapq
def dijkstras(graph,start):
    distances = {node:float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0,start)]

    while priority_queue:
        current_distance,current_node = heapq.heappop(priority_queue)

        if current_distance>distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance+weight

            if distance<distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue,(distance,neighbor))
    return distances
if __name__ == "__main__":
    example_graph = {
        'A': [('B', 4), ('D', 2)],
        'B': [('C', 3), ('D', 2), ('E', 1)],
        'C': [],
        'D': [('B', 1), ('E', 5)],
        'E': [('C', 2)]
    }
    
    start_node = 'A'
    shortest_paths = dijkstras(example_graph, start_node)
    
    print(f"Shortest distances from starting node '{start_node}':")
    for node, distance in shortest_paths.items():
        print(f"Distance to {node}: {distance}")