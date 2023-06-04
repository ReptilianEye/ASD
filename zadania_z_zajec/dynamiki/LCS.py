# najdłuższy wspólny podciag
# mając dane dwie tablice danych nalezy sprawdzic jaka dlugosc ma najdłuższy wspólny pociąg

def lcs(A, B):
    n = len(A)
    m = len(B)
    F = [[0]*m for _ in range(n)]
    if A[0] == B[0]:
        F[0][0] = 1
    for i in range(1, n):
        F[i][0] = F[i-1][0]
        if A[i] == B[0]:
            F[i][0] = 1
    for i in range(1, m):
        F[0][i] = F[0][i-1]
        if A[0] == B[i]:
            F[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            F[i][j] = max(F[i-1][j], F[i][j-1])
            if A[i] == B[j]:
                F[i][j] = max(F[i][j], F[i-1][j-1]+1)
    return F[n-1][m-1]


A = [2, 7, 3, 5, 10, 7]
B = [3, 4, 2, 7, 5, 7]
A = "abcde"
B = "ace"


A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
B = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(lcs(A, B))
