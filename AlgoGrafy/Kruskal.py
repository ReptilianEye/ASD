# Problem polega na znalezieniu minimalnego drzew rozpinającego (MST - minimal spanning tree), czyli takigoe, w którym suma krawedzi jest możliwie
# najmniejsza, ale aby graf nadal byl spójny
# Algorytm: podejscie polega na posortowaniu krawedzi, rosnaco, po wagach a nastepnie dodajemy je do grafu, jesli po dodaniu ich nie postanie cykl
# graf nieskierowany


def read_input(file="dane_mst.in"):
    with open(file) as file:
        n = int(file.readline().strip())
        G = [[] for _ in range(n)]
        for line in file:
            v, u, w = tuple(int(el) for el in line.strip().split(" "))
            G[v].append((u, w))
            # G[u].append((v, w)) #taka krawedz bylaby uznana za cykl, wiec nie ma sensu jej dodawac, a jedynie pamietac po wykonaniu algorytmu aby takie jak ona dodac
    return G


class Node:
    def __init__(self, val) -> None:
        self.parent = self
        self.rank = 0
        self.val = val


def findset(x):
    if x.parent is not x:
        x.parent = findset(x.parent)
    return x.parent


def union(x, y):
    x = findset(x)
    y = findset(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def prepare_edges(G):
    edges = []
    for v, nodes in enumerate(G):
        for u, w in nodes:
            edges.append((v, u, w))
    return sorted(edges, reverse=True, key=lambda x: x[2])


def add_lacking_edges(G):  # kiedy graf nieskierowany
    edges = []
    for v, nodes in enumerate(G):
        for u, w in nodes:
            edges.append((v, u, w))
    for v,u,w in edges:
        G[u].append((v,w))


def kruskal(G):
    n = len(G)
    e = 0
    mst = [[] for _ in range(n)]
    vert = [Node(i) for i in range(n)]
    edges = prepare_edges(G)
    while e < n-1:
        v, u, w = edges.pop()
        x = vert[v]
        y = vert[u]
        if findset(x) != findset(y):
            mst[v].append((u, w))
            union(x, y)
            e += 1
    add_lacking_edges(mst) #kiedy graf jest nieskierowany
    return mst


G = read_input()
for v, edges in enumerate(G):
    print(v, end=": ")
    for u in edges:
        print(u, end=" ")
    print()
print()
mst = kruskal(G)
for v, edges in enumerate(mst):
    print(v, end=": ")
    for u in edges:
        print(u, end=" ")
    print()
