# algorytm rozwiazuje problem maksymalnego przeplywu

from math import inf
from collections import deque


class Node:
    def __init__(self, capacity) -> None:
        self.flow = 0
        self.capacity = capacity


class Path:
    def __init__(self, v) -> None:
        self.min_capacity = inf
        self.v = v
        self.parent = None


def read_graph(edges, n):
    G = [[Node(0) for _ in range(n)] for _ in range(n)]
    for e in edges:
        s, t, c = e
        G[s][t].capacity = c
    return G


def bfs_by_capacity(G, s, t):
    n = len(G)
    vis = [False for _ in range(n)]
    Q = deque()
    Q.append(Path(s))
    while len(Q) > 0:
        curr_path = Q.popleft()
        u = curr_path.v
        vis[u] = True
        curr_path_cap = curr_path.min_capacity
        if u == t:
            return curr_path
        for v in range(n):
            if not vis[v] and G[u][v].capacity - G[u][v].flow > 0:
                new = Path(v)
                new.parent = curr_path
                new.min_capacity = min(
                    G[u][v].capacity - G[u][v].flow, curr_path_cap)
                Q.append(new)


def increment_flow(G, path, flow):
    while path.parent is not None:
        G[path.parent.v][path.v].flow += flow
        path = path.parent


def Ford_Fulkerson(G, s=0, t=6):
    n = len(G)
    flow = 0
    while True:
        path = bfs_by_capacity(G, s, t)  # Sciezka powiekszajaca
        if path is None:
            break
        flow += path.min_capacity
        increment_flow(G, path, path.min_capacity)
    return flow


edges = [
    (0, 1, 9),
    (0, 4, 9),
    (1, 2, 7),
    (1, 3, 3),
    (2, 3, 4),
    (2, 6, 6),
    (2, 6, 6),
    (3, 6, 9),
    (3, 5, 2),
    (4, 3, 3),
    (4, 5, 6),
    (5, 6, 8),
]
n = 7
G = read_graph(edges, n)
print(Ford_Fulkerson(G, 0, 6))
