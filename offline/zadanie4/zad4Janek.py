#Jan Masternak
#Na poczatek wykonujemy BFS, szukajac wszystkich najkrotszych sciezek z s do t (szukamy tylko do momentu, az znajdziemy wszystkie najkrotsze).
#Jezeli dojdziemy do t pierwszy raz to jako krawedz do usuniecia ustawiamy ta krawedz po ktorej wlasnie weszlismy do t.
#Jezeli po raz ktorys z kolei to zakladamy, ze nie ma takiej krawedzi.
#Pierwszy BFS zawsze da nam prawidlowa odpowiedz w 3 przypadkach:
#a) nie ma zadnej sciezki --> None
#b) jest tylko jedna najkrotsza sciezka --> ostatnia krawedz najkrotszej sciezki
#c) jest wiele najkrotszych sciezek, ale nie ma krawedzi, ktora nalezalaby do nich wszystkich --> None
#Zeby uwzglednic ostatni przypadek (wiele najkrotszych i istnieje przynajmniej jedna krawedz nalezaca do ich wszytkich) odpalamy kolejnego BFS.
#Ten BFS przechodzi tylko najkrotszymi sciezkami i jezeli okaze sie, ze pewien czas i wystepuje w tyko jednym wierzcholku a oraz i+1 w tylko jednym wierzcholku b, to usuniecie tej krawedzi psuje wszystkie najkrotsze sciezki>

from zad4testy import runtests
from queue import Queue


def longer(G, s, t):

    Q = Queue()
    edge_tbr = None
    n = len(G)
    vis = [False]*n
    mpl = [None]*n
    done = [False]*n
    vis[s] = True
    mpl[s] = 0
    mpl[t] = n**2
    is_accessible = False
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        n_v = len(G[u])
        for j in range(0, n_v):
            i = G[u][j]
            if vis[i] == False:
                if i == t:
                    edge_tbr = (u, i)
                    is_accessible = True
                vis[i] = True
                mpl[i] = mpl[u]+1
                if done[i] == False and mpl[i] < mpl[t]:
                    Q.put(i)
            elif i == t and vis[i] == True and mpl[i] == mpl[u]+1:
                edge_tbr = None
                break

        done[u] = True

    if edge_tbr == None and is_accessible == True:
        Q.put(t)
        ever_in_Q = [False]*n
        ever_in_Q[t] = True
        current_wave = mpl[t]-1
        vertice_for_cv = False
        if_last = False
        v = None

        while not Q.empty():
            u = Q.get()
            n_v = len(G[u])

            if mpl[u]-1 < current_wave:
                if vertice_for_cv != True and vertice_for_cv != False and current_wave == mpl[t]-1:
                    #edge_tbr = (vertice_for_cv,t)
                    if vertice_for_cv > t:
                        return (t, vertice_for_cv)
                    else:
                        return (vertice_for_cv, t)
                elif vertice_for_cv != True and vertice_for_cv != False and if_last == False:
                    v = vertice_for_cv
                    if_last = True
                    vertice_for_cv = False
                elif vertice_for_cv != True and vertice_for_cv != False and if_last == True:
                    if vertice_for_cv > v:
                        return (v, vertice_for_cv)
                    else:
                        return (vertice_for_cv, v)
                else:
                    if_last = False
                current_wave = mpl[u]-1
                vertice_for_cv = False

            for j in range(0, n_v):
                if mpl[G[u][j]] == mpl[u]-1 and ever_in_Q[G[u][j]] == False:
                    Q.put(G[u][j])
                    ever_in_Q[G[u][j]] = True
                    if vertice_for_cv != False and vertice_for_cv != True and vertice_for_cv != G[u][j]:
                        vertice_for_cv = True
                    elif vertice_for_cv == False:
                        vertice_for_cv = G[u][j]

    return edge_tbr


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
