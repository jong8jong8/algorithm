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
    # lowest_cost_path = {}
    # sorted_nodes = sorted(costs, key=costs.get)
    # for n in sorted_nodes:
    #     lowest_cost_path[n] = costs[n]
    # return lowest_cost_path


# the graph for Exercise 7.1 A
graphA = {}
graphA["start"] = {}
graphA["start"]["a"] = 5
graphA["start"]["b"] = 2

graphA["a"] = {}
graphA["a"]["c"] = 4
graphA["a"]["d"] = 2

graphA["b"] = {}
graphA["b"]["a"] = 8
graphA["b"]["d"] = 7

graphA["c"] = {}
graphA["c"]["d"] = 6
graphA["c"]["fin"] = 3

graphA["d"] = {}
graphA["d"]["fin"] = 1

graphA["fin"] = {}

# graphA = { 
#   "start": { "a": 5, "b": 2 },
#   "a": { "c": 4, "d": 2 },
#   "b": { "a": 8, "d": 7 },
#   "c": { "d": 6, "fin": 3 },
#   "d": { "fin": 1 },
#   "fin": { },
# } 


# the costs table for Exercise 7.1 A
infinity = float("inf")
costsA = {}
costsA["a"] = 5
costsA["b"] = 2
costsA["c"] = infinity
costsA["d"] = infinity
costsA["fin"] = infinity

# costsA = {
#   "a": 5,
#   "b": 2,
#   "c": infinity,
#   "d": infinity,
#   "fin": infinity,
# }


# the parents table for Exercise 7.1 A
parentsA = {}
parentsA["a"] = "start"
parentsA["b"] = "start"
parentsA["c"] = None
parentsA["d"] = None
parentsA["fin"] = None 

# parentsA = {
#   "a": "start",
#   "b": "start",
#   "c": None,
#   "d": None,
#   "fin": None,
# }


dijkstra(graphA, costsA, parentsA)
print(costsA)