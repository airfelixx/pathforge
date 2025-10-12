from math import radians, cos, sin, asin, sqrt

def determine_cost(orig, dest):
    lat1, lon1 = orig[0], orig[1]
    lat2, lon2 = dest[0], dest[1]

    lat1, lon1, lat2, lon2 = map(radians, [lat1,lon1,lat2,lon2])

    dX = lon2 - lon1
    dY = lat2 - lat1
    a = sin(dY/2)**2 + cos(lat1)*cos(lat2)*sin(dX/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371000
    cost = c*r
    return cost

def build_adjency_list(nodes, edges):
    graph = {}
    
    # Initialize all nodes in the graph
    for node_id in nodes:
        graph[node_id] = []
    
    # Add edges with costs (bidirectional)
    for u, v in edges:
        cost = determine_cost(nodes[u], nodes[v])
        graph[u].append((v, cost))
        graph[v].append((u, cost))  # Add reverse edge for bidirectional graph
    
    return graph
