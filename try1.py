import heapq
import math

# Define travel speeds (km/hr)
road_speed = 60
water_speed = 32

# Define the graph with nodes and coordinates
graph = {
    1: (70, 100),
    42: (100, 130),
    3: (120, 265),
    # Add more nodes and coordinates as needed
}

# Define the type of each node (road or water)
node_types = {
    1: "sea entrance",
    42: "junction",
    3: "headwater",
    # Add more nodes and types as needed
}

# Calculate travel time between two nodes based on distance and travel speed
def calculate_travel_time(node1, node2):
    distance = math.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)
    if "sea entrance" in node_types[node1] or "sea entrance" in node_types[node2]:
        travel_speed = water_speed
    else:
        travel_speed = road_speed
    travel_time = distance / travel_speed
    return travel_time

# Implement weighted shortest path search using Dijkstra's algorithm
def weighted_shortest_path_search(start, end):
    # Initialize priority queue and distances
    priority_queue = [(0, start)]
    visited = set()
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, neighbor_coordinates in graph.items():
            if neighbor != current_node:
                travel_time = calculate_travel_time(graph[current_node], neighbor_coordinates)
                if current_distance + travel_time < distances[neighbor]:
                    distances[neighbor] = current_distance + travel_time
                    heapq.heappush(priority_queue, (distances[neighbor], neighbor))

    # Reconstruct the quickest path
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        for neighbor, neighbor_coordinates in graph.items():
            if neighbor != current_node:
                travel_time = calculate_travel_time(graph[current_node], neighbor_coordinates)
                if distances[current_node] - travel_time == distances[neighbor]:
                    current_node = neighbor
                    break

    path.append(start)
    path.reverse()
    return path

# Example usage:
start_point = (70, 100)
end_point = (500, 290)
quickest_path = weighted_shortest_path_search(start_point, end_point)

# Print the quickest path
for node_id in quickest_path:
    print(f"Node {node_id} - Coordinates: {graph[node_id]}")


import networkx as nx
import pandas as pd
import math

# Load the dataset from water_data.xlsx
data = pd.read_excel("water_data.xlsx")

# Create a graph
G = nx.Graph()

# Add nodes to the graph
for idx, row in data.iterrows():
    G.add_node(row['Node'], x=row['x'], y=row['y'], linked=row['linked'], node_type=row['type'])

# Add edges to the graph
for idx, row in data.iterrows():
    if row['linked'] != 0:
        G.add_edge(row['Node'], data.iloc[row['linked'] - 1]['Node'])

# Function to calculate distance between two nodes
def distance(node1, node2):
    x1, y1 = G.nodes[node1]['x'], G.nodes[node1]['y']
    x2, y2 = G.nodes[node2]['x'], G.nodes[node2]['y']
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to find the shortest path for a ranger to inspect headwaters in an area
def shortest_path_with_dam(area_x_range, area_y_range):
    headwaters_in_area = [node for node in G.nodes if G.nodes[node]['node_type'] == 'headwater' and
                          area_x_range[0] <= G.nodes[node]['x'] <= area_x_range[1] and
                          area_y_range[0] <= G.nodes[node]['y'] <= area_y_range[1]]

    if not headwaters_in_area:
        return "No headwaters in the specified area."

    shortest_path = []
    visited_nodes = set()
    current_node = headwaters_in_area[0]

    while len(visited_nodes) < len(headwaters_in_area):
        shortest_distance = float('inf')
        next_node = None

        for neighbor in G.neighbors(current_node):
            if neighbor not in visited_nodes:
                dist = distance(current_node, neighbor)
                if dist < shortest_distance:
                    shortest_distance = dist
                    next_node = neighbor

        if next_node is not None:
            shortest_path.append((current_node, next_node))
            visited_nodes.add(current_node)
            current_node = next_node
        else:
            break

    # Convert the path to a human-readable format
    path_description = []
    for i in range(len(shortest_path)):
        node1, node2 = shortest_path[i]
        path_description.append(str(node1) + " -> " + str(node2))

    return "\n".join(path_description)

# Define the area's x and y ranges
area_x_range = (100, 250)
area_y_range = (100, 300)

# Find the shortest path for a ranger to inspect headwaters in the specified area
path_with_dam = shortest_path_with_dam(area_x_range, area_y_range)

print("Shortest path for ranger to inspect headwaters with dam:")
print(path_with_dam)
