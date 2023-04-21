def conv_to_im(G):  # lista sasiedztwa -> macierz incydencji:
    n = len(G)
    IM = [[False for _ in range(n)] for _ in range(n)]
    for v in range(n):
        for u in G[v]:
            IM[v][u] = True
    return IM


def print_edges(G):
    for i in range(len(G)):
        for el in G[i]:
            if el > i:
                print(i, el)
