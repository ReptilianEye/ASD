
# Piotr Rzadkowski
# algorytm bazuje na znajdywaniu najkrotszej sciezki do wierzcholka autorstwa Dijskry.
# wierzcholki zakrzywione sa zlepiane w jeden wierzcholek, a krawedzie od innych wierzcholkow zamieniane na jedna najmniejsza
# jesli algorytm skonczy update wierzcholka koncowego, konczy swoje dzialanie
#zlozonosc: O((E+V)*V)

from zad5testy import runtests
from math import inf


class Node:
    def __init__(self, dest, wage) -> None:
        self.dest = dest
        self.wage = wage


def find_lowest_undone(que):

    min_v = inf
    lowest = None
    for i, el in enumerate(que):
        if el[0] < min_v:
            min_v = el[0]
            lowest = i
    lowest = que.pop(lowest)
    return lowest


def shortest_paths_dijkstra(G, s, e):
    n = len(G)-1
    cost = [inf for _ in range(n+1)]
    Q = [False for _ in range(n+1)]
    cost[s] = 0
    q = [(0, s)]
    while len(q) > 0:
        v = find_lowest_undone(q)[1]
        # if v is None:
        # break
        Q[v] = True
        for u in G[v]:
            dest = u.dest
            if not Q[dest]:
                wage = u.wage
                if cost[dest] > cost[v] + wage:
                    cost[dest] = cost[v] + wage
                    q.append((cost[dest], dest))
            if dest == e:
                break

    return cost


def find_edge(nodes, to_find):
    for n in nodes:
        if n.dest == to_find:
            return True
    return False


def spacetravel(n, E, S, a, b):

    zakrzywione = [False for _ in range(n)]
    for v in S:
        zakrzywione[v] = True
    if zakrzywione[a] and zakrzywione[b]:
        return 0
    if zakrzywione[b]:
        a, b = b, a
        a = n

    G = [[] for _ in range(n+1)]
    for edge in E:
        v, u, wage = edge
        if zakrzywione[v] ^ zakrzywione[u]:
            if zakrzywione[u]:
                v, u = u, v
            if find_edge(G[u], n):
                for i in range(len(G[u])):
                    if G[u][i].dest == n:
                        G[u][i].wage = min(G[u][i].wage, wage)
                        break
                for i in range(len(G[n])):
                    if G[n][i].dest == u:
                        G[n][i].wage = min(G[n][i].wage, wage)
                        break
            else:
                G[u].append(Node(n, wage))
                G[n].append(Node(u, wage))
        elif not zakrzywione[u] and not zakrzywione[v]:
            G[v].append(Node(u, wage))
            G[u].append(Node(v, wage))
        else:
            pass

    costs = shortest_paths_dijkstra(G, a, b)
    if costs[b] == inf and zakrzywione[b]:
        costs[b] = costs[-1]
    if costs[b] == inf:
        result = None
    else:
        result = costs[b]
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=False)
