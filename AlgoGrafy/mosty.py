# most to krawedz, po usunieciu ktorej graf staje sie niespojny
#

from math import inf


def read_input(file="dane_mosty.in"):
    with open(file) as file:
        n = int(file.readline().strip())
        G = [[] for _ in range(n)]
        for line in file:
            v, u = tuple(int(el) for el in line.strip().split(" "))
            G[v].append(u)
            G[u].append(v)
    return G


def dfs_bridge(G, u, vis, parent, low, vis_time, time):

    vis[u] = True
    vis_time[u] = time
    low[u] = time

    for v in G[u]:
        if vis[v] == False:
            parent[v] = u
            dfs_bridge(G, v, vis, parent, low, vis_time, time+1)
            low[u] = min(low[u], low[v])

            if low[v] > vis_time[u]:
                print(u, v)

        elif v != parent[u]:
            low[u] = min(low[u], vis_time[v])


def bridge(G):
    n = len(G)
    visited = [False] * n
    vis_time = [inf] * n
    low = [inf] * n
    parent = [-1] * n

    for i in range(n):
        if visited[i] == False:
            dfs_bridge(G, i, visited, parent, low, vis_time, 1)
    print(vis_time)


G = read_input()
bridge(G)
