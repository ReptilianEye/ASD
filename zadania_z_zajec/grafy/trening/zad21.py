inf = float('inf')


def fw(G):
    n = len(G)
    cost = [[inf]*n for _ in range(n)]
    parent = [None]*n
    for v in range(n):
        for u, w in G[v]:
            cost[v][u] = w
    for i in range(n):
        cost[i][i] = 0

    for t in range(n-1):
        for v in range(n):
            for u in range(n):
                if cost[v][u] > cost[v][t] + cost[t][u]:
                    cost[v][u] = cost[v][t] + cost[t][u]
                    parent[v] = t



