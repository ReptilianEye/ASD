# Ścieżka Hamiltona w DAG’u

# rozw: zadanie sprowadza się do posortowania topologicznie wierzcholkow, a nastepnie sprawdzenia,
#  czy pomiedzy kazdymi sąsiadującymi po takim posortowaniu wierzcholkami, istenieje krawedz

from collections import deque


def top_sort(G, v, vis, q):
    vis[v] = True
    for u in G[v]:
        if not vis[u]:
            top_sort(G, u, vis, q)
    q.appendleft(v)


def hamilton_DAG(G):
    n = len(G)
    vis = [False]*n
    q = deque()
    for v in range(n):
        if not vis[v]:
            top_sort(G, v, vis, q)

    for i in range(n-1):
        if q[i+1] not in G[q[i]]:
            return False
    return True


G = [
    [1],
    [2],
    [3],
    [],
    [0, 2, 3],
]


print(hamilton_DAG(G))
