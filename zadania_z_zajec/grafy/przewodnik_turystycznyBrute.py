# Przewodnik turystyczny musi przeprowadzić grupe P turystów z miasta S do miasta K. Aby tam dojechać chce wybrać autobusy ale niestety każdy autobus z miasta x do
# y one ma ograniczoną pojemność ludzi. Na ile grupy po ile osób musi podzielić ludzi przewodnik, aby przewodnik mógł dojechać z miasta S do K ale aby grup było
# jak najmniej.

# algorytm: Algorytm polega na binarnie szukaniu najwiekszej możliwej przepływości i następnie sprawdzaniu czy taka ścieżka istnieje
# złożoność: O(logP*(V+E))


from collections import deque


class Node:
    def __init__(self, to, wage) -> None:
        self.to = to
        self.wage = wage


def prepare_graph():
    with open("edges_wages.txt") as file:
        n = int(file.readline())
        G = [[] for _ in range(n)]
        for line in file:
            edge = tuple(int(num) for num in line.strip().split(" "))
            G[edge[0]].append(Node(edge[1], edge[2]))
    return G


def find_biggest(G, S, E, T, indegrees):
    if indegrees[E] == 0:
        return None
    n = len(G)
    max_to_node = [0 for _ in range(n)]
    max_to_node[S] = T
    q = deque()
    q.append(S)
    while len(q) > 0 and indegrees[E] > 0:
        v = q.popleft()
        for u in G[v]:
            indegrees[u.to] -= 1
            max_to_node[u.to] = max(
                max_to_node[u.to], min(u.wage, max_to_node[v]))
            if indegrees[u.to] == 0:
                q.append(u.to)
    return max_to_node[E]


def tour(G, S, E, P):
    l = 1
    p = P
    while l <= P:
        s = (l+p)//2
    # return find_biggest(G, S, E, P, indegrees)


G = prepare_graph()
print(tour(G, 0, 6, 100))
