from zad2testy import runtests


def czy_same_zera(t):
    for el in t:
        if el != 0:
            return False
    return True


def wyzeruj(t, end, z_lewej):
    n = len(t)
    if z_lewej:
        i = 0
        step = 1
    else:
        i = n-1
        step = -1
    while i != end:
        t[i] = 0
        i += step
    t[end] = 0


def stop_snieg(t):
    n = len(t)
    for i in range(n):
        t[i] = max(t[i]-1, 0)


def generuj_TL(t):
    n = len(t)
    Tl = [0 for _ in range(n)]
    Tl[0] = t[0]
    for i in range(1, n):
        Tl[i] = t[i]+Tl[i-1]
    Tl.insert(0, 0)  # wartownik
    return Tl


def generuj_TP(t):
    n = len(t)
    Tl = [0 for _ in range(n)]
    Tl[n-1] = t[n-1]
    for i in range(n-2, -1, -1):
        Tl[i] = t[i]+Tl[i+1]
    Tl.append(0)  # wartownik
    return Tl


def generuj_ilosc_niezerowych(t):
    n = len(t)
    niezerowe = [0 for _ in range(len(t))]
    for i in range(1, n-1):

        niezerowe[i] = niezerowe[i-1]
        if t[i] != 0:
            niezerowe[i] += 1
    for i in range(n-2, 0, -1):
        niezerowe[i] = min(t[i-1], t[i+1])
        if t[i] != 0:
            niezerowe[i] += 1
    return niezerowe


# t = [1, 2, 0, 0, 2]
# print(generuj_ilosc_niezerowych(t))


def ilosc_niezerowych(t, i, n):
    w_lewo = 0
    j = i-1
    while j >= 0:
        if t[j] != 0:
            w_lewo += 1
        j -= 1
    w_prawo = 0
    j = i+1
    while j < n:
        if t[j] != 0:
            w_prawo += 1
        j += 1
    return min(w_lewo, w_prawo)


def snow(t):
    n = len(t)
    s = 0
    while not czy_same_zera(t):
        Tl = generuj_TL(t)
        Tp = generuj_TP(t)
        czy_z_lewej = True
        pnp = -1
        wnp = -1
        l = 0
        p = n-1
        while l <= p:
            i = l
            aktualne = t[i]-min(Tl[i], Tp[i+1])-ilosc_niezerowych(t,i, n)
            if wnp < aktualne:
                wnp = aktualne
                pnp = i
                czy_z_lewej = True if min(
                    Tl[i], Tp[i+1]) == Tl[i] else False
            i = p
            aktualne = t[i]-min(Tl[i], Tp[i+1])-ilosc_niezerowych(t,i, n)
            if wnp < aktualne:
                wnp = aktualne
                pnp = i
                czy_z_lewej = True if min(
                    Tl[i], Tp[i+1]) == Tl[i] else False
            l += 1
            p -= 1
        s += t[pnp]
        wyzeruj(t, pnp, czy_z_lewej)
        stop_snieg(t)
    return s


# S = [1, 7, 3, 4, 1]
# print(snow(S))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=False)
