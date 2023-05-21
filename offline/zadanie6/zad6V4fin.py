from zad6testy import runtests
from collections import deque


def update_path(path, S, T):
    for i in range(0, len(path), 2):
        S[path[i]] = path[i+1]
        T[path[i+1]] = path[i]


def poszerz(v, S, T, G):
    vis = [False]*len(G)
    q = deque()
    q.append((v, []))
    while len(q) > 0:
        v, path = q.popleft()
        vis[v] = True
        for u in G[v]:
            if T[u] is None:
                update_path(path+[v, u], S, T)
                return
            if not vis[T[u]]:
                q.append((T[u], path+[v, u]))


def binworker(G):
    n = len(G)
    R = [None]*n
    T = [None]*n
    for i in range(n):
        poszerz(i, R, T, G)

    s = 0
    for el in T:
        if el is not None:
            s += 1
    return s


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=False)
