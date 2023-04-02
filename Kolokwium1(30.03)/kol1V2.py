from kol1testy import runtests



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
    k = n-k
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


def find_k_elV2(A, l, r, fin):
    k = l+fin
    while True:
        q = partition(A, l, r)
        if q == k:
            return A[q]
        elif q < k:
            l = q+1
        else:
            r = q-1


# res = find_k_el()

def tidy(A, x, l, r):
    for i in range(l, r):
        if A[i] == x:
            A[l-1], A[i] = A[i], A[l-1]
            return


def ksum(T, k, p):
    n = len(T)
    s = 0
    prime = T[:n-p+1]
    fin = p-k
    for i in range(n-p+1):
        l=i
        r=p+i-1
        val = find_k_elV2(T, i, r, fin)
        s += val
        tidy(T,prime[i],l+1,r+1)
    return s


# T = [7, 9, 1, 5, 8, 6, 2, 12]
# print(ksum(T, 4, 5))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=False)
