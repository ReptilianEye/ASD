from zad5testy import runtests

from math import inf


def find_lowest_undone(cost, Q):
    min_v = inf
    lowest = None
    for i in range(len(cost)):
        if not Q[i] and cost[i] < min_v:
            min_v = cost[i]
            lowest = i
    return lowest


def shortest_paths_dijkstra(G, s, e, zakrzywione):
    n = len(G)-1
    # to_check = []
    # for i in range(n+1):
        # if G[e][i] != 0 and G[e][i] != -1:
            # to_check.append(i)
    cost = [inf for _ in range(n+1)]
    Q = [False for _ in range(n+1)]
    cost[s] = 0
    # prev = [None for _ in range(n)]

    while True:
        v = find_lowest_undone(cost, Q)
        if v is None:
            break
        Q[v] = True
        for u in range(n+1):
            if G[v][u] != 0:
                wage = G[v][u]
                dest = u
                if not Q[dest]:
                    if cost[dest] > cost[v] + wage:
                        cost[dest] = cost[v] + wage
                if dest == e:
                    break

    return cost


def spacetravel(n, E, S, a, b):

    zakrzywione = [False for _ in range(n)]
    for v in S:
        zakrzywione[v] = True
    if zakrzywione[a] and zakrzywione[b]:
        return 0
    if zakrzywione[b]:
        a, b = b, a
        a = n

    G = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for edge in E:
        v, u, wage = edge
        if zakrzywione[v]:
            G[u][v] = -1
            G[n][u] = min(G[n][u], wage) if G[n][u] != 0 else wage
            G[u][n] = G[n][u]
        elif zakrzywione[u]:
            G[v][u] = -1
            G[n][v] = min(G[n][v], wage) if G[n][v] != 0 else wage
            G[v][n] = G[n][v]
        else:
            G[v][u] = wage
            G[u][v] = wage

    costs = shortest_paths_dijkstra(G, a, b, zakrzywione)
    if costs[b] == inf and zakrzywione[b]:
        costs[b] = costs[-1]
    if costs[b] == inf:
        result = None
    else:
        result = costs[b]
    return result


# E = [(0, 1, 5),
#      (1, 2, 21),
#      (1, 3, 1),
#      (2, 4, 7),
#      (3, 4, 13),
#      (3, 5, 16),
#      (4, 6, 4),
#      (5, 6, 1)]
# S = [0, 2, 3]
# a = 1
# b = 5
# n = 7
# n = 7
# E = [(0, 1, 5), (1, 2, 21), (1, 3, 1), (2, 4, 7),
#      (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]
# S = [0, 2, 3]
# a = 1
# b = 2

# n = 7
# E = [(0, 1, 5), (1, 2, 21), (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]
# S = [0, 2]
# a = 1
# b = 6


# res = spacetravel(n, E, S, a, b)
# print(res)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=False)
