from math import inf
from queue import PriorityQueue


def read_path(array, c):
    path = [c]
    while array[c] != None:
        path.append(array[c])
        c = array[c]
    # path.append(c)
    return path[::-1]


def which_path_to_read(a, b, array_a, array_b, c):
    if a < b:
        return read_path(array_a, c)
    else:
        return read_path(array_b, c)


def relax(u, v, w, previous_vertices, previous_edge, distance, Q):
    if distance[v] > distance[u]+w:
        distance[v] = distance[u]+w
        previous_vertices[v] = u
        previous_edge[v] = w
        Q.put((distance[v], v))


def trip(G, a, b, who_starts, previous_vertice):
    n = len(G)

    for u in G[a]:
        if b == u:
            return 0

    Q = PriorityQueue()
    distance = [inf for _ in range(n)]
    distance[a] = 0
    previous_edge = [None for _ in range(n)]
    previous_edge[a] = who_starts
    visited = [False for _ in range(n)]
    Q.put((0, a))
    while not Q.empty():
        u = Q.get()[1]
        # if w >= distance[b]:
        # return distance[b]
        if not visited[u]:
            visited[u] = True
            #if u == 7: print(u,previous_edge[u])
            if previous_edge[u] == 0:
                for v in G[u]:
                    relax(u, v[0], v[1], previous_vertice,
                          previous_edge, distance, Q)
            else:
                for v in G[u]:
                    relax(u, v[0], 0, previous_vertice,
                          previous_edge, distance, Q)

    print(distance)
    return distance[b]


def initialize(G, a, b):
    n = len(G)
    previous_vertice_a = [None for _ in range(n)]
    previous_vertice_b = [None for _ in range(n)]
    a_starts = trip(G, a, b, 0, previous_vertice_a)
    b_starts = trip(G, a, b, inf, previous_vertice_b)
    if a_starts < b_starts:
        who_starts = "Alice"
    else:
        who_starts = "Bob"
    return min(a_starts, b_starts), who_starts, which_path_to_read(a_starts, b_starts, previous_vertice_a, previous_vertice_b, b)


Graph1 = [[(2, 60), (3, 50)],
          [(2, 10), (3, 70)],
          [(0, 60), (1, 10), (3, 100)],
          [(0, 50), (1, 70), (2, 100)]
          ]
# for i in range(len(Graph1)):
#     for u in Graph1[i]:
#         print(i, u[0],u[1])
Graph2 = [[(21, 10), (6, 15), (5, 90), (2, 30)],
          [(8, 20), (6, 40), (7, 50), (21, 75)],
          [(0, 30), (3, 20), (4, 20)],
          [(2, 20), (4, 90), (10, 15)],
          [(2, 20), (3, 90), (10, 20)],
          [(0, 90), (6, 10), (7, 80)],
          [(1, 40), (5, 10)],
          [(1, 50), (5, 80), (8, 10), (9, 15), (12, 10)],
          [(1, 20), (9, 150)],
          [(8, 150), (7, 15)],
          [(4, 20), (3, 15), (11, 10), (13, 55)],
          [(10, 10), (17, 10)],
          [(7, 10), (16, 20), (17, 10)],
          [(10, 55), (14, 35), (15, 10)],
          [(13, 35), (15, 70), (20, 20)],
          [(13, 10), (18, 30)],
          [(12, 20), (20, 5)],
          [(11, 10), (12, 10)],
          [(15, 30), (19, 30)],
          [(18, 30), (20, 30)],
          [(16, 5), (14, 20), (19, 30)],
          [(0, 10), (1, 75)]
          ]
# for i in range(len(Graph2)):
#     for u in Graph2[i]:
#         print(i, u[0], u[1])
print(initialize(Graph1, 0, 1))
# print(initialize(Graph2, 0, 20))
