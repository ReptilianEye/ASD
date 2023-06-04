# longest increasing sequence
# znalezc najdluzszy rosnacy podciag w tablicy A

def lisV1(A):
    n = len(A)
    F = [1]*n
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j]+1 > F[i]:
                F[i] = F[j]+1
    return max(F)


def bsearch(B, x,n):
    l = 0
    r = n-1
    while l <= r:
        s = (l+r)//2
        if x > B[s]:
            l = s+1
        else:
            r = s-1
    return l


def lis_nlogn(A):
    n = len(A)
    inf = float('inf')
    F = [inf]*n
    lis_len = 0
    for el in A:
        p = bsearch(F, el,lis_len)
        F[p] = el
        if p == lis_len:
            lis_len += 1

    return lis_len


A = [2, 1, 4, 2, 1, 5, 2, 7, 8, 3]
print(lisV1(A))
print(lis_nlogn(A))
