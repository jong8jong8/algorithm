from collections import deque

def is_seller(name):
    return name[-1] == 'm'

def bfs(name):
    queue = deque()
    