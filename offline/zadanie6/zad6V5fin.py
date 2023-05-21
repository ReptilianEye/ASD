from zad6testy import runtests
from collections import deque


def update_path(path, T):
    for i in range(0, len(path), 2):
        T[path[i+1]] = path[i]


def augment(v,  T, G):
    vis = [False]*len(G)
    q = deque()
    q.append((v, []))
    while len(q) > 0:
        v, path = q.popleft()
        vis[v] = True
        for u in G[v]:
            if T[u] is None:
                update_path(path+[v, u], T)
                return True
            if not vis[T[u]]:
                q.append((T[u], path+[v, u]))
    return False


def binworker(G):
    n = len(G)
    T = [None]*n
    s = 0
    for i in range(n):
        if(augment(i, T, G)):
            s += 1

    return s


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=False)
