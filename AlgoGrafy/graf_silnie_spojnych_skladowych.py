from collections import deque


class SCC:  # strongly connected component
    def __init__(self) -> None:
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


def create_ssc_graph(G):
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

    return scc_graph
