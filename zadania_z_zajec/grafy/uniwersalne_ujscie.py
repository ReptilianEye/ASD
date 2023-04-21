# zadanie polega na znalezieniu takiego wierzcholka, do ktorego mozna dojsc bezposrednio z kazdego innego i nie wychodzi z niego zadna krawedz
# macierz incydencji, graf skierowany
# pomysl polega na przechodzeniu po macierzy incydencji zaczynajac od [0,0] w taki sposob, ze jesli natrafimy na 0 to [+1,0] a jesli 1 to [0,+1]

from pomocne import conv_to_im
# co jesli nasz wierzcholek ktorego szukamy to 0


def universal_output(G):
    G = conv_to_im(G)
    n = len(G)
    row = col = 0
    while row < n and col < n:
        if G[row][col] or row == col:
            row += 1
        else:
            col += 1
    if row < n:
        return False

    for i in range(n):
        if not G[i][col]:
            if row == n:
                row = i
            else:
                return False
    for i in range(n):
        if G[row][i]:
            return False
    return True
