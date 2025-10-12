import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start]=0

    parents = {node: None for node in graph}
    
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        if current_dist > distances[current_node]:
            continue

        for neighbor, cost in graph[current_node]:
            distance = current_dist + cost

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    path = []
    node = end
    
    # Check if destination is reachable
    if distances[end] == float('inf'):
        return [], float('inf')
    
    while node is not None:
        path.append(node)
        node = parents[node]
    path.reverse()

    return path, distances[end]
