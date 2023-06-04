# problem pakowania plecaka

def knupsack(W, P, B):  # W - wagi, P - ceny, B - maksymalna waga
    n = len(W)  # ilosc przedmiotów
    F = [[0 for b in range(B+1)] for i in range(n)]
    for b in range(W[0], B+1):
        F[0][b] = P[0]

    for b in range(B+1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            if b-W[i] >= 0:
                F[i][b] = max(F[i][b], F[i-1][b-W[i]] + P[i])

    return F[n-1][B]


W = [1, 4, 20]
P = [2, 10, 50]
B = 25
res = knupsack(W, P, B)
print(res)
