# nalezy policzyc ilosc spojnych skladowych grafy nieskierowanego

def count_connected_components(G):
    n = len(G)
    visited = [False for _ in range(n)]

    def DFS_visit(G, v):
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                DFS_visit(G, u)

    cc_count = 0
    for v in range(n):
        if not visited[v]:
            DFS_visit(G, v)
            cc_count += 1
    return cc_count


G = [
    [],
    [3],
    [],
    [1]
]
print(count_connected_components(G))
