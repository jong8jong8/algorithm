def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)


# the graph for Exercise 7.1 C
graph = {}
graph["start"] = {}
graph["start"]["a"] = 2
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 2
graph["a"]["fin"] = 2

graph["b"] = {}
graph["b"]["a"] = 2

graph["c"] = {}
graph["c"]["b"] = -1 # negative weight
graph["c"]["fin"] = 2

graph["fin"] = {}

# the costs table for Exercise 7.1 C
infinity = float("inf")
costs = {}
costs["a"] = 2
costs["b"] = 2
costs["c"] = infinity
costs["fin"] = infinity

# the parents table for Exercise 7.1 C
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["fin"] = None 

dijkstra(graph, costs, parents)
print(costs)
print(parents)