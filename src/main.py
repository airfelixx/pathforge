from parser import parse_osm
from graph import build_adjency_list
from algorithms import dijkstra

def main():
    nodes, edges = parse_osm("../maps_ignore/basic_city_graph.osm")
    graph = build_adjency_list(nodes, edges)
    start = int(input("Origin:"))
    end = int(input("Destination:"))
    path, distance = dijkstra(graph, start, end)
    
    if distance == float('inf'):
        print(f"No path found from {start} to {end}")
    else:
        print(f"Shortest path: {path}")
        print(f"Total distance: {distance:.2f} meters")
    return 0

main()
