# nalezy sprawdzic czy z wierzcholka x mozna dojsc do wierzcholka y w taki sposob, ze idziemy tylko po krawedziach o malejacej wadze
import queue


class Node:
    def __init__(self, destination, wage) -> None:
        self.destination = destination
        self.wage = wage


def descending_path(G, x, y):
    n = len(G)
    for i in range(n):
        G[i] = sorted(G[i], key=lambda x: x.wage)
    q = queue.Queue()
    x = Node(x, 10**10)
    q.put(x)
    while not q.empty():
        u = q.get()
        if u.destination == y:
            return True
        for v in G[u.destination]:
            if v.wage < u.wage:
                q.put(v)
    return False
