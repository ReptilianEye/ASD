# Dana jest tablica A parami różnych elementów. Należy sprawdzić, czy istnieje taka ich kombinacja,
# aby ich suma była równa T

def if_sum_exists(A, T):
    n = len(A)
    F = [[False]*(T+1) for _ in range(n)]
    for i in range(n):
        F[i][0] = True
    F[0][A[0]] = True
    for t in range(1, T+1):
        for i in range(1, n):
            F[i][t] = F[i-1][t]
            if t-A[i] >= 0:
                F[i][t] = F[i][t] or F[i-1][t-A[i]]
    return F[n-1][T]


A = [3, 4, 2, 7, 8]
T = 12
print(if_sum_exists(A,T))
