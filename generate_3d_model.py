import osmnx as ox

# Define the school location (change this!)
place_name = "Warsaw, Poland"  # Replace with your school city

# Download the map data
graph = ox.graph_from_place(place_name, network_type="all")
ox.save_graphml(graph, "map_data.graphml")

print("Downloaded OSM data successfully!")

# Save the OSM data for later processing
with open("map_data.txt", "w") as file:
    file.write("OSM data saved for 3D conversion.")
