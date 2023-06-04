# Dana jest kwota T i lista nominałów monet N, których można użyć. Należy zwróć najmniejszą liczbę monet,
# którą należy użyć, aby wydać kwote T.

def coin_changeV1(T, N):
    n = len(N)
    F = [[float('inf')]*(T+1) for _ in range(n)]
    for i in range(n):
        F[i][0] = 0

    for t in range(N[0], T+1):
        if t % N[0] == 0:
            F[0][t] = t//N[0]

    for t in range(1, T+1):
        for i in range(1, n):
            F[i][t] = F[i-1][t]
            if t-N[i] >= 0:
                F[i][t] = min(F[i][t], 1+F[i][t-N[i]])

    return F[n-1][T]


def coin_changeV2(T, N): #without 2D tab
    n = len(N)
    F = [float('inf')]*(T+1)
    F[0] = 0

    for t in range(N[0], T+1):
        if t % N[0] == 0:
            F[t] = t//N[0]

    for t in range(1, T+1):
        for i in range(1, n):
            if t-N[i] >= 0:
                F[t] = min(F[t], 1+F[t-N[i]])

    return F[T]


T = 15
N = [1, 3, 5]
print(coin_changeV2(T, N))
