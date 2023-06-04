# Graf z parami różnymi wagami z zakresu 1-|E |, sprawdzić czy dla danych wierzchołków x, y istnieje ścieżka z x do y po której przechodzimy po krawędziach o coraz mniejszych wagach
from collections import deque
from math import inf


def descending_path(G, s, t):
    q = deque()
    q.append((s, inf))
    while q:
        v, prev_e = q.popleft()
        if v == t:
            return True
        for u, w in G[v]:
            if w < prev_e:
                q.append((u, w))
    return False
