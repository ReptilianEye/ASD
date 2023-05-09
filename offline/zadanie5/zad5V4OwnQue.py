import random
from zad5testy import runtests

from math import inf

from queue import PriorityQueue


class Que:
    def __init__(self,nodes_n) -> None:
        self.que = [None for _ in range(nodes_n)]
        self.n = 0

    def left(self, i):
        return i*2+1

    def right(self, i):
        return i*2+2

    def parent(self, i):
        return (i-1)//2

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        min_i = i
        if l < self.n and self.que[min_i][0] > self.que[l][0]:
            min_i = l
        if r < self.n and self.que[min_i][0] > self.que[r][0]:
            min_i = r
        if min_i != i:
            self.que[min_i], self.que[i] = self.que[i], self.que[min_i]
            self.heapify(min_i)

    def put(self, new):
        if self.n < len(self.que):
            self.que[self.n] = new
        else:
            self.que.append(new)
        self.n += 1
        for i in range((self.n // 2) - 1, -1, -1):
            self.heapify(i)
        # self.que[0], self.que[self.n] = self.que[self.n], self.que[0]
        self.heapify(self.n-1)

    def get(self):
        res = self.que[0]
        if self.n > 0:
            self.que[self.n-1], self.que[0] = self.que[0], self.que[self.n-1]
        self.n -= 1
        self.heapify(0)
        # for i in range(self.n//2-1, -1, -1):
            # self.heapify(i)
        return res

    def empty(self):
        return self.n == 0


# q = Que()
# for i in range(10):
#     new = (random.randint(1, 100),  chr(ord("a")+i))
#     q.put(new)
# while not q.empty():
#     print(q.get())


class Node:
    def __init__(self, dest, wage) -> None:
        self.dest = dest
        self.wage = wage


# def find_lowest_undone(cost, Q):
#     min_v = inf
#     lowest = None
#     for i in range(len(cost)):
#         if not Q[i] and cost[i] < min_v:
#             min_v = cost[i]
#             lowest = i
#     return lowest


def shortest_paths_dijkstra(G, s, e):
    n = len(G)-1
    # q = PriorityQueue()
    q = Que(n)
    cost = [inf for _ in range(n+1)]
    Q = [False for _ in range(n+1)]
    cost[s] = 0
    q.put((0, s))
    # prev = [None for _ in range(n)]

    while not q.empty():
        # v = find_lowest_undone(cost, Q)
        v = q.get()[1]
        # if v is None:
        # break
        Q[v] = True
        for u in G[v]:
            dest = u.dest
            if not Q[dest]:
                wage = u.wage
                if cost[dest] > cost[v] + wage:
                    cost[dest] = cost[v] + wage
                    q.put((cost[dest], dest))
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
