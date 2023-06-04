from collections import deque
# 2.Znaleźć wszystkie spójne składowe


def bfs(G, i, vis):
    q = deque()
    q.append(i)
    while q:
        u = q.pop()
        vis[u] = True
        for v in G[u]:
            if not vis[v]:
                q.append(v)


def connected_components(G):
    n = len(G)
    vis = [False]*n

    count = 0
    for i in range(n):
        if not vis[i]:
            bfs(G, i)
            count += 1
    return count


G = [
    [1],  # 0
    [0],  # 1
    [3],  # 2
    [4, 2],  # 3
    [3],  # 4
]
print(connected_components(G))
