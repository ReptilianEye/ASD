# zadanie polega na znaleźeniu ściezki Hamilona w grafie typu DAG (Directed Acyclic Graph)
# aby to wykonać należy posortować wierzchołki topologicznie. Po takim posortowaniu, aby ściezka istniała to pomiedzy każdymi dwoma sąsiadującymi wierzchołkami musi istnieć krawędź. Jeśli tak nie będzie to nie będzie, to na pewno będzie co najmniej jeden wierzchołek który sie ominie

# graf jest listą sąsiedztwa
from collections import deque


def dfs_rec(v, G, vis, sorted_notes):
    vis[v] = True
    for u in G[v]:
        if not vis[u]:
            dfs_rec(u, G, vis, sorted_notes)
    sorted_notes.appendleft(v)


def topological_sort(G, n):
    sorted_notes = deque()
    vis = [False for _ in range(n)]
    for v in range(n):
        if not vis[v]:
            dfs_rec(v, G, vis, sorted_notes)

    return sorted_notes


def solve(G):
    n = len(G)
    sorted_notes = topological_sort(G, n)
    for i in range(n-1):
        if sorted_notes[i+1] not in G[sorted_notes[i]]:
            return False
    return list(sorted_notes)


G = [
    [1, 2, 3],
    [2],
    [3, 4],
    [4],
    [],
]
print(solve(G))
