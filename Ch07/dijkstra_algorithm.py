# the graph
graph = {}                  # {}
graph["start"] = {}         # { "start": {} } 
graph["start"]["a"] = 6     # { "start": { "a": 6 } } 
graph["start"]["b"] = 2     # { "start": { "a": 6, "b": 2 } } 

graph["a"] = {}             # { "start": { "a": 6, "b": 2 }, "a": {} } 
graph["a"]["fin"] = 1       # { "start": { "a": 6, "b": 2 }, "a": { "fin": 1 } } 

graph["b"] = {}             # { "start": { "a": 6, "b": 2 }, "a": { "fin": 1 }, "b": {} } 
graph["b"]["a"] = 3         # { "start": { "a": 6, "b": 2 }, "a": { "fin": 1 }, "b": { "a": 3 } } 
graph["b"]["fin"] = 5       # { "start": { "a": 6, "b": 2 }, "a": { "fin": 1 }, "b": { "a": 3, "fin": 5 } } 

graph["fin"] = {}           # { "start": { "a": 6, "b": 2 }, "a": { "fin": 1 }, "b": { "a": 3, "fin": 5 }, "fin": {} } 

# the costs table
infinity = float("inf")     # int("inf") is NOT valid!
costs = {}                  # {}
costs["a"] = 6              # { "a": 6 }
costs["b"] = 2              # { "a": 6, "b": 2 }
costs["fin"] = infinity     # { "a": 6, "b": 2, "fin": infinity }

# the parents table
parents = {}                # {}
parents["a"] = "start"      # { "a": "start" }
parents["b"] = "start"      # { "a": "start", "b": "start" }
parents["fin"] = None       # { "a": "start", "b": "start", "fin": None }

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Find the lowest-cost node that you haven't processed yet.
node = find_lowest_cost_node(costs)
# If you've processed all the nodes, this while loop is done.
while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node...
        if costs[n] > new_cost:
            # ... update the cost for this node.
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor.
            parents[n] = node
    # Mark the node as processed.
    processed.append(node)
    # Find the next node to process, and loop.
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)