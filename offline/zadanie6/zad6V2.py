from zad6testy import runtests


def dfs(v, R, T, G, vis):
    for u in G[v]:
        if T[u] == -1:
            R[v] = u
            T[u] = v
            return True

    for u in G[v]:
        if not vis[u]:
            vis[u] = True
            res = dfs(T[u], R, T, G, vis)
            vis[u] = False
            if res:
                R[v] = u
                T[u] = v
                return True
    return False


def poszerz(v, R, T, G):
    vis = [False]*len(G)
    dfs(v, R, T, G, vis)


def binworker(G):
    n = len(G)
    R = [-1]*n
    T = [-1]*n
    for i in range(n):
        poszerz(i, R, T, G)
    s = 0
    for el in R:
        if el != -1:
            s += 1
    return s


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=False)
