# Znaleźć cykl Eulera i go zwrócić
# rozw: nalezy sprawdzic czy kazdy wierzcholek jest parzystego stopnia a nastepnie przejsc graf.


def euler_path(G, v, path, n):
    for i in range(n):
        if G[v][i]:
            G[v][i] = 0

# postac macierzowa


def euler(G):
    n = len(G)
    for v in range(n):
        if len(sum(G[v])) % 2 == 1:
            return False


def euler_dfs(G):
    s = 0
    n = len(G)
    # left = len(G[s])
    cycle = []

    def euler_rec(G, v):
        nonlocal n, cycle
        cycle.append(v)
        for u in range(n):
            if G[v][u] == 1:
                G[v][u] = 0
                G[u][v] = 0
                euler_rec(G, u)

    for i in range(n):
        if G[s][i]:
            passed_edge = (i, s)
            G[s][i] = 0
            G[i][s] = 0
            break
    euler_rec(G, s)
    cycle.append(s)
    print(cycle)


G = [

[1,3],
[0,3],
[3,4],
[0,1,2,4],
[2,3]
]

n = len(G)
G_M = [[0 for _ in range(n)] for _ in range(n)]
for v, nodes in enumerate(G):
    for u in nodes:
        G_M[v][u] = 1
euler_dfs(G_M)


###############
def Euler(M):
    n = len(M)
    how_far = [0 for _ in range(0, n)]
    e_path = []

    def DFS(M, u):
        nonlocal e_path
        nonlocal how_far
        for i in range(how_far[u], len(M)):
            if M[u][i] == True:
                M[u][i] = False
                M[i][u] = False
                how_far[u] = i+1
                DFS(M, i)
        e_path.append(u)

    for i in range(0, n):
        counter = 0
        for j in range(0, n):
            if M[i][j] == True:
                counter += 1
        if counter % 2 != 0:
            return False

    DFS(M, 0)
    return e_path


Graph = [[1, 9],
         [0, 2, 4, 3],
         [1, 4],
         [1, 4, 7, 8],
         [1, 2, 3, 9],
         [6, 7],
         [5, 7],
         [3, 5, 6, 8],
         [3, 7],
         [0, 4]
         ]

n = len(Graph)
Matrix = [[False for _ in range(0, n)] for _ in range(0, n)]
for i in range(0, n):
    for j in range(0, len(Graph[i])):
        Matrix[i][Graph[i][j]] = True

# print(Matrix)

print(Euler(Matrix))
