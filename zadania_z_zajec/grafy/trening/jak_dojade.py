from queue import PriorityQueue
inf = float('inf')


def dij(G, a):
    n = len(G)
    vis = [False]*n
    cost = [inf]*n
    q = PriorityQueue()
    cost[a] = 0
    q.put((0, a))
    while q:
        _, v, p = q.get()
        vis[v] = True
        for u in range(n):
            if not vis[u] and G[v][u] <= p:
                if cost[u] > cost[v] + G[v][u]:
                    cost[u] = cost[v] + G[v][u]
                    q.put((cost[u], u))
    return cost


def jak_dojade(G, P, d, a, b):
    n = len(G)
    stacje = [False]*n
    for s in P:
        stacje[s] = True
    G2 = [None for _ in range(len(P))]
    for i, p in enumerate(P):
        cost_p = dij(G, p)
        G2[i] = cost_p
    for i in range(n):
        for j in range(n):
            if G2[i][j] > d:
                G2[i][j] = -1
    res = dij(G2, a)
    return res[b]
