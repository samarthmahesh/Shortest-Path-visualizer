import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Define cities and distances
city_names = ["Bangalore", "Kochi", "Chennai", "Hyderabad", "Vellore"]
distances = {
    ("Bangalore", "Kochi"): 500,
    ("Bangalore", "Chennai"): 350,
    ("Bangalore", "Hyderabad"): 600,
    ("Bangalore", "Vellore"): 200,
    ("Kochi", "Chennai"): 650,
    ("Kochi", "Hyderabad"): 900,
    ("Kochi", "Vellore"): 750,
    ("Chennai", "Hyderabad"): 500,
    ("Chennai", "Vellore"): 300,
    ("Hyderabad", "Vellore"): 400
}

# Function to create graph from distances
def create_graph(distances):
    G = nx.Graph()
    for (city1, city2), dist in distances.items():
        G.add_edge(city1, city2, weight=dist)
    return G

# Dijkstra's algorithm to find shortest path
def dijkstra(G, start, end):
    queue = [(0, start)]
    distances = {node: float('inf') for node in G.nodes}
    distances[start] = 0
    parent = {node: None for node in G.nodes}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in G.neighbors(current_node):
            weight = G[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Reconstruct path
    path = []
    node = end
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()

    return distances[end], path

# Visualize the graph and the shortest path
def visualize_graph(G, path):
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    # Draw nodes and edges
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Highlight the shortest path
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=4)
    
    plt.title("Shortest Path Visualization")
    plt.show()

# Main execution
def main():
    # Create the graph
    G = create_graph(distances)

    # User input for starting and destination cities
    print("Cities: 0: Bangalore, 1: Kochi, 2: Chennai, 3: Hyderabad, 4: Vellore")
    start = int(input("Enter the starting city (0-4): "))
    end = int(input("Enter the destination city (0-4): "))
    
    start_city = city_names[start]
    end_city = city_names[end]

    # Calculate the shortest path
    distance, path = dijkstra(G, start_city, end_city)
    
    # Display the result
    print(f"Shortest distance from {start_city} to {end_city} is {distance} km.")
    print("Path:", " -> ".join(path))
    
    # Visualize the graph and the path
    visualize_graph(G, path)

# Run the program
if __name__ == "__main__":
    main()
