# Zad1: Dana jest tablica zawierająca n liczb z zakresu[0...n^2-1]. Napisz algorytm, który posortuje taką
# tablicę w czasie O(n).

# Pomysł na algorytm:
# Algorytm jest oparty na radix sort. Liczby z takiego zakresu można przedstawić w jako liczbę ( //n , % n). Posortowanie takiej tablicy będzie więc posrtowaniem tablicy liczb po %n a potem po %n^2. Ponieważ mamy dwa sortowania które mozna zrobić w czasie O(n) algorytm ma złożoność liniową.


import string
import math
from random import randint


def zad1(t):
    n = len(t)
    # sort by %n
    counts = [0]*n
    for i in range(n):
        counts[t[i] % n] += 1
    for i in range(1, n):
        counts[i] += counts[i-1]
    b = [0]*n
    for i in range(n-1, -1, -1):
        b[counts[t[i] % n]-1] = t[i]
        counts[t[i] % n] -= 1

    # sort by n//2
    counts = [0]*n
    for i in range(n):
        counts[b[i] // n] += 1
    for i in range(1, n):
        counts[i] += counts[i-1]
    for i in range(n-1, -1, -1):
        t[counts[b[i] // n]-1] = b[i]
        counts[b[i] // n] -= 1

# -----------------------------------------------


# Zadanie: dana jest tablica A n liczb i wiadomo, że moc zbioru wartości liczb tej tablicy wynosi logn. (Czyli jest dużo powtórzeń)
# Algorytm: pomysł jest oparty na zliczaniu. Skoro zbiór wartości jest wielkości logn to też tablica zliczeń też będzie tak miała.
# Zrobimy tak: każda wartości z tablicy T będziemy dodawali do tablicy C (zliczeń) w taki sposób, że jeśli ta wartość już w niej jest to
# dodajemy tylko jej licznik. Potem tak jak w zwykłym sortowaniu przez zliczanie.
class zliczenia:
    def __init__(self, val) -> None:
        self.val = val
        self.count = 1


def b_search(C, n, x):
    l = 0
    r = n-1
    while l <= r:
        s = l + (r-l)//2
        if C[s].val == x:
            return s
        if C[s].val > x:
            r = s-1
        else:
            l = s+1
    return -1


def print_t(C):
    for el in C:
        if el is None:
            break
        print(el.val, el.count)
    print("---")


def zad2(A):
    n = len(A)
    C = [None]*math.ceil(math.log2(n))
    cnt = 0
    for el in A:
        index = b_search(C, cnt, el)
        if index == -1:
            C[cnt] = zliczenia(el)
            i = cnt
            while i > 0 and C[i-1].val > C[i].val:
                C[i-1], C[i] = C[i], C[i-1]
                i -= 1
            cnt += 1
        else:
            C[index].count += 1
        # print_t(C)
    for i in range(1, cnt):
        C[i].count += C[i-1].count

    res = [0]*n
    for i in range(n-1, -1, -1):
        poz = b_search(C, cnt, A[i])
        if poz == -1:
            print("ERR", A[i])
            return
        res[C[poz].count-1] = A[i]
        C[poz].count -= 1
    return res


# -----------------------------------------------

# zad3: zaproponowac strukture danych, ktora dla nieograniczonej pamieci obsluguje następujące funkcje:
# init() - zeruje tablice - O(1)
# add() - dodaje element (np. liczbe) i zwraca ilość jej wystąpień - O(1)
# count() - zwraca liczbe różnych elementów w tablicy - O(1)

# ponieważ w pythonie nie da się zaalokować pamięci, bez inicjowania tablicy (tj. bez czyszczenia jej),
# zasymuluje to tworząc tablice z losowymi elementami
# ponieważ nie istnieje coś takiego jak nieograniczona pamieć tablica będzie obsługiwała tylko wartości od 0-inf (inf=np.100)
inf = 100


class infinite_tab:

    class element():
        def __init__(self, val) -> None:
            self.val = val
            self.el_cnt = randint(0, inf)
            self.stack_address = randint(0, inf)
            self.tab_address = randint(0, inf)

    def __init__(self, inf=inf) -> None:
        self.cnt = 0
        self.stack = []  # potrzebne, aby wiedzieć jakie wartości będę mieć
        self.inf = inf
        self.T = [self.element(randint(0, self.inf))
                  for _ in range(self.inf)]  # wypełniam śmieciami aby móc założyć, że złożoność O(1) (bez inicjowania tablicy)

    def init(self):
        self.__init__()

    def add(self, val):
        if val >= self.inf:
            print("ZA DUŻY")
            return
        in_tab = self.T[val]
        in_stack = in_tab.stack_address
        if type(in_stack) is not int and in_stack.tab_address == in_tab:
            self.T[val].el_cnt += 1
        else:
            new_t = self.element(val)
            new_s = self.element(val)
            new_t.el_cnt = 1
            new_t.stack_address = new_s  # elementy w tablicy i w stosie na siebie wskazuja
            new_s.tab_address = new_t
            self.stack.append(new_s)  # dodajemy element do stosu i do tablicy
            self.T[val] = new_t
            self.cnt += 1  # zwiekszamy ilosc różnych elementów
        return self.T[val].el_cnt

    def count(self):
        return self.cnt


# zad4: należy sprawdzić czy dwa słowa są anagramami (z liter jednego słowa mozna stworzyć drugie)
# algorytm: zliczymy litery jednego słowa, zredukujemy drugim i sprawdzimy, czy tablica zliczeń jest pusta
def zad4(w1, w2):
    if len(w1) != len(w2):
        return False
    w1 = w1.lower()
    w2 = w2.lower()
    n = len(string.ascii_lowercase)
    counts = [0]*n
    for c in w1:
        counts[ord(c)-ord("a")] += 1
    for c in w2:
        counts[ord(c)-ord("a")] -= 1
        if counts[ord(c)-ord("a")] < 0:
            return False
    return True

# -----------------------------------------------
# zad5: celem jest znalezienie w tablicy T, takich dwóch elementów x i y, aby ich różnica była jak największa i aby nie istniało takie z, że
# x < z < y (jest pomiedzy nimi)
# algorytm: pomysł jest na wykorzystanie sortowania kubełkowego. Dzielimy dane na n kubełków. Jeśli nie ma pustego kubełka to oznacza, że dane
# są posortowane, więc wystarczy przejśc po tablicy i znaleźć najwiekszą różnice miedzy sąsiednimi wyrazami.
# Jeśli nie to wiemy, że porównujemy max z lewego kubełka i min z lewego i szukamy największej różnicy


def zad5(A):
    n = len(A)
    buckets = [[] for _ in range(n)]
    for el in A:
        buckets[el]
