# zadanie polega na sprawdzeniu w grafie skierowanym czy istnieje taki wierzolek z ktorego istnieje sciezka do każdego innego. Rozszerzeniem tego zadania jest znalezenie każdego takiego

# algorym: pierwszym krokiem jest podzial grafu na silnie spojne skladowe. Dzieki temu dostanimy graf DAG. Dzieki temu mozemy go posortować topologicznie. Kiedy go posortujemy topologicznie to jesli można dojść z pierwszej silnie spojnej skladowej do kazdej innej spojnej skladowej to znaczy, że istnieje taki wierzcholek i są to wszystkie które należą do tej silnie spójnej składowej

from collections import deque


class SCC:  # strongly connected component
    def __init__(self) -> None:
        # self.id = id
        self.nodes = []
        self.neighbours = []


def reverse_graph(G):
    rev_g = [[] for _ in range(len(G))]
    for i, v_nb in enumerate(G):
        for nb in v_nb:
            rev_g[nb].append(i)
    return rev_g


def prepare_order(v, G, vis, finish_order):
    vis[v] = True
    for u in G[v]:
        if not vis[u]:
            prepare_order(u, G, vis, finish_order)
    finish_order.appendleft(v)


def separate_scc(v, G, vis, curr_SCC):
    vis[v] = True
    for u in G[v]:
        if not vis[u]:
            separate_scc(u, G, vis, curr_SCC)
    curr_SCC.nodes.append(v)


def connect_sccs(SCCs, G):
    n = len(G)
    nodes_to_SCC = [None for _ in range(n)]
    for i, v in enumerate(SCCs):
        for u in v.nodes:
            nodes_to_SCC[u] = i

    for v in range(n):
        for u in G[v]:
            if nodes_to_SCC[u] != nodes_to_SCC[v] and nodes_to_SCC[u] not in SCCs[nodes_to_SCC[v]].neighbours:
                SCCs[nodes_to_SCC[v]].neighbours.append(nodes_to_SCC[u])
    return [scc.neighbours for scc in SCCs]


def dfs_topsort(v, G, vis, sorted_notes):
    vis[v] = True
    for u in G[v]:
        if not vis[u]:
            dfs_topsort(u, G, vis, sorted_notes)
    sorted_notes.appendleft(v)


def topological_sort(G):
    n = len(G)
    sorted_notes = deque()
    vis = [False for _ in range(n)]
    for v in range(n):
        if not vis[v]:
            dfs_topsort(v, G, vis, sorted_notes)

    return sorted_notes


def is_path_to_all_sccs(v, G):
    n = len(G)
    vis = [0 for _ in range(n)]
    q = deque()
    q.append(v)
    while len(q) > 0:
        v = q.popleft()
        vis[v] = 1
        for u in G[v]:
            if vis[u] == 0:
                q.append(u)

    return sum(vis) == n


def solve(G):
    n = len(G)

    # finding strongly connected components
    rev_G = reverse_graph(G)
    finish_order = deque()
    vis = [False for _ in range(n)]
    for v in range(n):
        if not vis[v]:
            prepare_order(v, G, vis, finish_order)
    vis = [False for _ in range(n)]
    SCCs = []
    for v in finish_order:
        if not vis[v]:
            new_SCC = SCC()
            separate_scc(v, rev_G, vis, new_SCC)
            SCCs.append(new_SCC)

    # creating a graph from strongly connected components
    scc_graph = connect_sccs(SCCs, G)
    # sort topologicaly sccs
    sorted_sccs = topological_sort(scc_graph)

    # check there is a path from first topologicaly scc to all other sccs
    resp = is_path_to_all_sccs(sorted_sccs[0], scc_graph)
    if not resp:
        return False
    return SCCs[sorted_sccs[0]].nodes


def make_graph():
    with open("edges.txt") as file:
        n = int(file.readline())
        G = [[] for _ in range(n)]
        for line in file:
            pair = tuple(int(num) for num in line.strip().split(" "))
            G[pair[0]].append(pair[1])
    return G


G = make_graph()
# G = [
#     [3],
#     [0],
#     [1],
#     [2, 4],
#     [5],
#     [6],
#     [4],
# ]
res = solve(G)
print(res)
