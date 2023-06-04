def is_bipartial(G):
    n = len(G)
    colors = [0] * n

    def dfs(G, v, color):
        nonlocal colors

        colors[v] = color

        for u in G[v]:
            if colors[u] == 0:
                if not dfs(G, u, not color):
                    return False
            else:
                if colors[u] == color:
                    return False

        return True

    return dfs(G, 0, False)


G = [
    [1, 3],  # 0
    [0, 2],  # 1
    [1, 3],  # 2
    [0, 2],  # 3
]

G2 = [
    [1, 3, 2],  # 0
    [0, 2],  # 1
    [1, 3, 0],  # 2
    [0, 2],  # 3
]

print(is_bipartial(G))
print(is_bipartial(G2))
