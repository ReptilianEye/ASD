from kol1testy import runtests
# Piotr Rzadkowski
# Algorytm bazuje na funkcji partition. Dla kazdej kopii p elementowego przedzialu tablicy sprawdza, ktory elementy bylby
# k-ty najwiekszy a nastepnie go zwraca. Element zostaje dodany do sumy. Sytuacja jest powtarzana dla kazdego elementu dostajemy wynik.
# Poniewaz przedzialow jest w zaokragleniu w gore n, znajdywanie k-tej najwiekszej liczby w przedziale p elementowym jest liniowe
# Algorytm ma zlozonosc O(n*p)


def partition(A, l, r):
    x = A[r]

    i = l-1
    for j in range(l, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def find_k_el(A, k):
    n = len(A)
    # k = n-k
    l = 0
    r = n-1
    while True:
        q = partition(A, l, r)
        if q == k:
            return A[q]
        elif q < k:
            l = q+1
        else:
            r = q-1


def ksum(T, k, p):
    n = len(T)
    s = 0
    fin = p-k
    for i in range(n-p+1):
        val = find_k_el(T[i:p+i], fin)
        print(val)
        s += val
    return s


T = [5, 8, 3, 1, 2, 8, 5, 4, 3, 2, 1]
p = 4
k = 2
print(ksum(T,k,p))
# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(ksum, all_tests=True)
