# algorytm:
# graf ktory posiada cykl Eulera musi byc spojny i kazdy wierzcholek musi miec parzysty stopien
# jesli spelnione sa te dwa warunki to wystarczy isc po grafie dfs az do momentu kiedy nie ma juz krawedzi do odwiedzenia

def conv_to_im(G):  # lista sasiedztwa -> macierz incydencji:
    n = len(G)
    IM = [[0 for _ in range(n)] for _ in range(n)]
    for v in range(n):
        for u in G[v]:
            IM[v][u] = 1
    return IM


def dfs_rec(v, G, n, last_visited, path):
    for i in range(last_visited[v], n):
        if G[v][i] == 1:
            last_visited[v] = i
            G[v][i] = G[i][v] = 0
            dfs_rec(i, G, n, last_visited, path)
    path.append(v)


def cykl_eulera(G):
    n = len(G)
    G = conv_to_im(G)
    total = 0
    for i in range(n):
        total += sum(G[i])
        if total % 2 == 1:
            return False

    last_visited = [0 for _ in range(n)]
    path = []
    dfs_rec(0, G, n, last_visited, path)
    if total//2 + 1 != len(path):
        return False
    return path


G = [
    [2, 1],
    [0, 2, 3, 4],
    [0, 1],
    [1, 4],
    [1, 3],

]
res = cykl_eulera(G)
print(res)
