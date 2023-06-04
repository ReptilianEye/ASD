def bf(G, s=0):
    n = len(G)
    cost = [float('inf')]*n
    cost[s] = 0
    parent = [None]*n
    for _ in range(n-1):
        for v in range(n):
            for u, w in G[v]:
                if cost[u] > cost[v] + w:
                    cost[u] = cost[v]+w
                    parent[u] = v

    for v in range(n):
        for u, w in G[v]:
            if cost[u] > cost[v] + w:
                print("Cykl ujemny")
                return False
    return cost
