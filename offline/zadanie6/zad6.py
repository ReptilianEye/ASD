from zad6testy import runtests

from math import inf
from collections import deque


class Node:
    def __init__(self, dest, capacity) -> None:
        self.dest = dest
        self.flow = 0
        self.capacity = capacity


class Path:
    def __init__(self, v) -> None:
        self.min_capacity = inf
        self.v = v
        self.my_poz = None
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
        u = curr_path.v[0]
        vis[u] = True
        curr_path_cap = curr_path.min_capacity
        if u == t:
            return curr_path
        for i, v in enumerate(G[u]):
            if not vis[v.dest] and v.capacity - v.flow > 0:
                new = Path(v.dest)
                new.my_poz = (u, i)
                new.parent = curr_path
                new.min_capacity = min(
                    v.capacity - v.flow, curr_path_cap)
                Q.append(new)


def increment_flow(G, path, flow):
    while path is not None:
        u,v = path.my_poz
        G[u][v].flow += flow
        path = path.parent


def mflow(G, s=0, t=6):  # finds max flow
    n = len(G)
    flow = 0
    while True:
        path = bfs_by_capacity(G, s, t)  # Sciezka powiekszajaca
        if path is None:
            break
        flow += path.min_capacity
        increment_flow(G, path, path.min_capacity)
    return flow


def prepare(M):
    n = len(M)
    G = [[Node(i+1, 1) for i in range(n)]]
    for node_nbors in M:
        G.append([Node(el+n+1, 1) for el in node_nbors])
    for _ in range(n):
        G.append([Node(2*n+1, 1)])
    G.append([])
    return G


M = [[0, 1, 3],
     [2, 4],
     [0, 2],
     [3],
     [3, 2]]


def binworker(M):
    n = len(M)
    G = prepare(M)
    res = mflow(G, 0, 2*n+1)
    return res
  




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=False)
