from math import inf


class Node:
    def __init__(self, dest, wage) -> None:
        self.dest = dest
        self.wage = wage


def find_lowest_undone(cost, Q):
    min_v = inf
    lowest = None
    for i in range(len(cost)):
        if not Q[i] and cost[i] < min_v:
            min_v = cost[i]
            lowest = i
    return lowest


def shortest_paths_dijkstra(G, s):
    n = len(G)
    cost = [inf for _ in range(n)]
    Q = [False for _ in range(n)]
    cost[s] = 0
    prev = [None for _ in range(n)]

    while True:
        v = find_lowest_undone(cost, Q)
        if v is None:
            break
        Q[v] = True
        for u in G[v]:
            dest = u.dest
            wage = u.wage
            if not Q[dest]:
                if cost[dest] > cost[v] + wage:
                    cost[dest] = cost[v] + wage
                    prev[dest] = v

    return cost, prev


def read_data():
    with open("dane_dj.in") as file:
        s,n,edges = tuple(int(num) for num in file.readline().strip().split(" "))
        G = [[] for _ in range(s+n)]
        for line in file:
            v, u, wage = tuple(int(num) for num in line.strip().split(" "))
            G[v].append(Node(u, wage))
    return G

G = read_data()
cost, prev = shortest_paths_dijkstra(G,0)
print(cost)
print(prev)