import queue

# zakladam, ze jesli graf jest niespojny, ale kazda spojna skladowa jest grafem dwudzielnym to caly graf jest dwudzielny
# jesli by tak nie bylo to zamiast fora w lini 12 nalezaloby po zakonczeniu petli while sprawdzic czy kazdy wierzcholek w tablicy colors ma kolor.
# Jesli nie ma to znaczy, ze graf jest niespojny



def bipartite(G):
    n = len(G)
    colors = [None for _ in range(n)]

    q = queue.Queue()

    for v in range(n):
        if colors[v] is None:
            q.put(v)
            colors[v] = 1
            while not q.empty():
                u = q.get()
                for v in G[u]:
                    if colors[v] is None:
                        colors[v] = -colors[u]
                        q.put(v)
                    elif colors[v] == colors[u]:
                        return False
    return True


G = [
    [],
    [2, 3],
    [1, 3],
    [1, 2]
]

print(bipartite(G))