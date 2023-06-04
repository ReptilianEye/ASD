# Przewodnik turystyczny musi przeprowadzić grupe P turystów z miasta S do miasta K. Aby tam dojechać chce wybrać autobusy ale niestety każdy autobus z miasta x do
# y one ma ograniczoną pojemność ludzi. Na ile grupy po ile osób musi podzielić ludzi przewodnik, aby przewodnik mógł dojechać z miasta S do K ale aby grup było
# jak najmniej.

# algorytm: algorytm polega na przejściu grafu algorytmem bfs szukając takiej ścieżki dla której min(wagi krawedzi scieżki) jest najwieksza z wszystkich ścieżek z
# S do K, ale w taki sposób, że możemy wyjść z wierzchołka tylko wtedy kiedy przerobiliśmy już wszystkie krawędzie wchodzące do tego wierzchołka.
# Złożoność: O(V + E)


from queue import PriorityQueue


def prepare_graph(file="edges_wages.txt"):
    with open(file) as file:
        n = int(file.readline().strip())
        G = [[] for _ in range(n)]
        for line in file:
            v, u, w = tuple(int(num) for num in line.strip().split(" "))
            G[v].append((u, w))
    return G


def print_path(path, v):
    if v is None:
        return
    print_path(path, path[v])
    print(v,end=" ")


def find_biggest(G, S, E, P):
    n = len(G)
    vol = [0]*n
    vis = [False]*n
    par = [None]*n
    q = PriorityQueue()
    vol[S] = P
    q.put((vol[S], S))
    while not q.empty():
        _, v = q.get()
        if v == E:
            break
        vis[v] = True
        for u, w in G[v]:
            if not vis[u]:
                if vol[u] < min(w, vol[v]):
                    vol[u] = min(w, vol[v])
                    par[u] = v
                    q.put((vol[u], u))
    return vol,par


def tour(G, S, E, P):
    vol,par = find_biggest(G, S, E, P)
    print_path(par,E)
    print()
    return vol[E]


G = prepare_graph()
print(tour(G, 0, 6, 100))
