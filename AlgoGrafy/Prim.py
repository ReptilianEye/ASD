# Problem polega na znalezieniu minimalnego drzew rozpinającego (MST - minimal spanning tree), czyli takigoe, w którym suma krawedzi jest możliwie
# najmniejsza, ale aby graf nadal byl spójny
# Algorytm: opiera się na algorytmie Dijskry, a właściwie jest jego kopią
# graf nieskierowany


from queue import PriorityQueue
from math import inf


def read_input(file="dane_mst.in"):
    with open(file) as file:
        n = int(file.readline().strip())
        G = [[] for _ in range(n)]
        for line in file:
            v, u, w = tuple(int(el) for el in line.strip().split(" "))
            G[v].append((u, w))
            G[u].append((v, w)) 
    return G


def mst(v, cost, parent):  # recreates mst tree
    n = len(cost)
    edges = []
    for i in range(n):
        if i != v:
            edges.append((i, parent[i], cost[i]-cost[parent[i]]))
    G = [[] for _ in range(n)]
    for v, u, w in edges:
        G[v].append((u, w))
        G[u].append((v, w))  # if undirected
    return G


def prim(G, v=0):
    s=v
    n = len(G)
    q = PriorityQueue()
    vis = [False for _ in range(n)]
    cost = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    cost[v] = 0
    q.put((0, v))
    while not q.empty():
        v = q.get()[1]
        vis[v] = True
        for u, w in G[v]:
            if not vis[u]:
                if cost[u] > cost[v] + w:
                    cost[u] = cost[v] + w
                    parent[u] = v
                    q.put((cost[u], u))
    return mst(s, cost, parent)


G = read_input()
for v, edges in enumerate(G):
    print(v, end=": ")
    for u in edges:
        print(u, end=" ")
    print()
print()
mst = prim(G)
for v, edges in enumerate(mst):
    print(v, end=": ")
    for u in edges:
        print(u, end=" ")
    print()
