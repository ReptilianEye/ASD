# algorytm:


# nie bardzo mam pomysl jak przestawic krawedzie nie robiac macierzy
# pomysl - mamy krawedzie znajdujemy wyszukiwaniem binarnym

from collections import deque


class Node:
    def __init__(self, destination) -> None:
        self.dest = destination
        self.vis = False


def convert_graph(G):
    for i in range(len(G)):
        for j in range(len(G[i])):
            G[i][j] = Node(G[i][j])


def dfs_rec(e_poz, G, path):
    G[e_poz[0]][e_poz[1]].vis = True
    G[]
    v = G[e_poz[0]][e_poz[1]].dest
    for i in range(len(G[v])):
        if not G[v][i].vis:
            dfs_rec((v, i), G, path)
    path.appendleft(v)


def cykl_eulera(G):
    n = len(G)
    convert_graph(G)
    path = deque()
    for i in range(n):
        for j in range(len(G[i])):
            if not G[i][j].vis:
                dfs_rec((i, j), G, path)

    print(path)


G = [
    [1, 3],
    [0, 2],
    [1, 3],
    [2, 0],
]
for i in range(len(G)):
    for el in G[i]:
        if el > i:
            print(i, el)
cykl_eulera(G)
