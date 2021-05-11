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


# the graph for Exercise 7.1 B
graph = {}
graph["start"] = {}
graph["start"]["a"] = 10

graph["a"] = {}
graph["a"]["c"] = 20

graph["b"] = {}
graph["b"]["a"] = 1

graph["c"] = {}
graph["c"]["b"] = 1
graph["c"]["fin"] = 30

graph["fin"] = {}

# the costs table for Exercise 7.1 B
infinity = float("inf")
costs = {}
costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs["fin"] = infinity

# the parents table for Exercise 7.1 B
parents = {}
parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["fin"] = None 

dijkstra(graph, costs, parents)
print(costs)
print(parents)