from math import inf
from queue import PriorityQueue


def bf(G, s=0):
    n = len(G)
    prev = [None] * n
    cost = [inf]*n
    cost[s] = 0
    for _ in range(n):
        was_change = False
        for u in range(n):
            for v, w in G[u]:
                if cost[v] > cost[u]+w:
                    cost[v] = cost[u]+w
                    prev[v] = u
                    was_change = True
        if not was_change:
            return cost, prev

    # checking if negative cycle
    for u in range(n):
        for v, w in G[u]:
            if cost[v] > cost[u]+w:
                print("Ujemny cykl!")
                return False
    return cost, prev


def read_data():
    with open("dane_bf.in") as file:
        n = int(file.readline().strip())
        G = [[] for _ in range(n)]
        for line in file:
            v, u, wage = tuple(int(num) for num in line.strip().split(" "))
            G[v].append((u, wage))
    return G


G = read_data()
cost, prev = bf(G)
print(cost)
print(prev)
