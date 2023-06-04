# Algorytm znajduje najkrotsza sciezke dla kazdej pary wierzcholkow w czasie O(n^3)

from math import inf


def neg_cycle(G):  # returns true if there was a negative cycle
    n = len(G)
    for i in range(n):
        if G[i][i] < 0:
            return True
        if G[i][i] != 0:
            print("Something is wrong in", i, G[i][i])
    return False


def fw(G):  # Floyd Warshall
    n = len(G)
    d = [[inf]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != inf:
                d[i][j] = G[i][j]
    for k in range(n):
        for v in range(n):
            for u in range(n):
                if d[v][u] > d[v][k] + d[k][u]:
                    d[v][u] = d[v][k] + d[k][u]

    if neg_cycle(d):
        print("Ujemny cykl!")
        return None
    return d


def print_path(u, v, p):
    if u == v:
        print(u, end=" ")
        return True
    if p[u][v] == None:
        print("nie ma sciezki")
        return False
    res = print_path(u, p[u][v], p)
    if res:
        print(v, end=" ")
    return res




def fw_path(G):  # Floyd Warshall
    n = len(G)
    d = [[inf]*n for _ in range(n)]
    p = [[None]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != inf:
                d[i][j] = G[i][j]
                p[i][j] = i
    for k in range(n):
        for v in range(n):
            for u in range(n):
                if d[v][u] > d[v][k] + d[k][u]:
                    d[v][u] = d[v][k] + d[k][u]
                    p[v][u] = p[k][u]

    if neg_cycle(d):
        print("Ujemny cykl!")
        return None
    return d, p


def read_input(file="dane_fw.in"):
    G = []
    with open(file) as file:
        n = int(file.readline().strip())
        G = [[inf]*n for _ in range(n)]
        for line in file:
            u, v, w = tuple(int(el) for el in line.strip().split(" "))
            if (u == v == 0):
                print(w)
            G[u][v] = w
    for i in range(n):
        G[i][i] = 0
    return G


G = read_input()
fw(G)
d, p = fw_path(G)
print_path(4, 2, p)
