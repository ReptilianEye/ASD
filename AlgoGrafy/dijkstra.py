from math import inf
from queue import PriorityQueue


def dijkstra(G, s=0):
    n = len(G)
    vis = [False] * n
    prev = [None] * n
    cost = [inf]*n
    q = PriorityQueue()
    cost[s] = 0
    q.put((0, s))
    while not q.empty():
        v = q.get()[1]  # ignoring parameter needed for priority que
        vis[v] = True
        for u, wage in G[v]:
            if not vis[u]:
                if cost[u] > cost[v] + wage:
                    cost[u] = cost[v] + wage
                    prev[u] = v
                    q.put((cost[u],u))

    return cost, prev


def read_data():
    with open("dane_dj.in") as file:
        n = int(file.readline().strip())
        G = [[] for _ in range(n)]
        for line in file:
            v, u, wage = tuple(int(num) for num in line.strip().split(" "))
            G[v].append((u, wage))
    return G


G = read_data()
cost, prev = dijkstra(G)
print(cost)
print(prev)
