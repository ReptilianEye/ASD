# 3.	Znany operator linii komórkowych splajtuje i usuwa swoje urządzenia, ze względów technologicznych urządzenia należy usuwać pojedynczo, a graf ma pozostać spójny
# zadanie polega na podaniu kolejnosci usuwania wierzcholkow, w taki sposob, aby ani przez chwile graf nie stal sie niespojny

# rozw - kolejnosc taka moze wyznaczyc dfs. Jesli po przerobieniu wierzcholka dodamy go to kolejki, dostaniemy prawidlowa kolejnosc

from collections import deque

result = deque()


def dfs(G, v, vis):
    vis[v] = True
    for u in G[v]:
        if not vis[u]:
            dfs(G, u, vis)
    result.append(v)


def solve(G):
    n = len(G)
    vis = [False]*n
    for v in range(n):
        if not vis[v]:
            dfs(G, v, vis)
    print(result)


G = [
    [1],
    [0, 2, 3],
    [1, 3],
    [1, 2, 4],
    [3]
]
solve(G)
