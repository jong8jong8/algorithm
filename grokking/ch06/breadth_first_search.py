from collections import deque

def is_seller(name):
    return name[-1] == 'm'

def bfs(graph, name):
    queue = deque()
    searched = set()
    queue += graph[name]
    while queue:
        person = queue.popleft()
        if person not in searched:
            if is_seller(person):
                return person
            else:
                queue += graph[person]
                searched.add(person)
    return "nobody"

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

mango_seller = bfs(graph, "you")
print(f"The mango seller is {mango_seller}!")
