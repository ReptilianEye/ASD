# nalezy sprawdzic czy w grafie nieskierowanym jest cykl 4 elementowy
# mozna zauwazyc, że jeśli taki cykl istnieje to może on być pokazany jako kwadrat
# w takim kwadracie, jeśli bedziemy patrzyli na dwa wierzcholki na przekatnych, pozostaje sprawdzic czy te wierzcholki maja pare tych samych sasiadow
# jesli tak, to mamy cykl, a jesli nie to szukamy dalej
# pare wierzcholkow musimy generowac w czasie n^2 i sprawdzenie czy dwa wierzcholki maja pare tych samych sasiadow jest liniowe, stad zlozonosc ostateczna n^3
# wykorzystujemy macierz incydencji, graf nieskierowany


from pomocne import conv_to_im


def n4_cycles(G):
    n = len(G)
    G = conv_to_im(G)
    for v in range(n):
        for u in range(n):
            if v != u and not G[u][v] and not G[v][u]:
                cnt = 0
                for i in range(n):
                    if G[v][i] and G[u][i]:
                        cnt += 1
                    if cnt >= 2:
                        return True
    return False


G = [
    [1, 3],
    [0, 2, 3, 4],
    [1, 3, 4],
    [0, 1, 2],
    [1, 2]
]
print(n4_cycles(G))
