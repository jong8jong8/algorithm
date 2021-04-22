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


# the graph for Exercise 7.1 A
graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}

# graph = { 
#   "start": { "a": 5, "b": 2 },
#   "a": { "c": 4, "d": 2 },
#   "b": { "a": 8, "d": 7 },
#   "c": { "d": 6, "fin": 3 },
#   "d": { "fin": 1 },
#   "fin": { },
# } 


# the costs table for Exercise 7.1 A
infinity = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

# costs = {
#   "a": 5,
#   "b": 2,
#   "c": infinity,
#   "d": infinity,
#   "fin": infinity,
# }


# the parents table for Exercise 7.1 A
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None 

# parents = {
#   "a": "start",
#   "b": "start",
#   "c": None,
#   "d": None,
#   "fin": None,
# }


dijkstra(graph, costs, parents)
print(costs)
print(parents)