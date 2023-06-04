# Piotr Rzadkowski
# Zadanie polega na znalezieniu licznosci najwiekszego skojarzenia.
# Aby to zrobić wykorzystuje algorytm, znajdujacy sciezki powiekszajace, ktory w sposob zachlanny stara sie dobrac pare
# dla wierzcholka z jednej pary wierzcholka na drugi. Jesli ktorys z sasiadow jest wolny, to ta krawedz jest zaznaczana
# a w innym przypadku sprawdzamy, czy mozna wierzcholkom dopisanym przypisac inna sciezke.
#Złożoność: O(N*(E+N))
from zad6testy import runtests
from collections import deque


def update_path(path, T):
    for source, dest in path:
        T[dest] = source


def augment(v,  T, G):
    vis = [False]*len(G)
    q = deque()
    q.append((v, []))
    while len(q) > 0:
        v, path = q.popleft()
        vis[v] = True
        for u in G[v]:
            if T[u] is None:
                update_path(path+[(v, u)], T)
                return True
            if not vis[T[u]]:
                q.append((T[u], path+[(v, u)]))
    return False


def binworker(G):
    n = len(G)
    T = [None]*n
    s = 0
    que = list(range(n))
    que.sort(key=lambda x: len(G[x]))
    for i in que:
        if augment(i, T, G):
            s += 1

    return s


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=True)
