# dana jest szachownica NxN, taka ze kazde pole ma swoj koszt. Należy znaleźć jaki jest koszt najkrótszej trasy
# z (0,0) do (N-1,N-1). Król może iść tylko w dól i w prawo.


from random import randint


def king(board):
    n = len(board)
    cost_board = [[None]*n for _ in range(n)]
    cost_board[0][0] = board[0][0]
    for i in range(1, n):
        cost_board[i][0] = board[i][0] + cost_board[i-1][0]
        cost_board[0][i] = board[0][i] + cost_board[0][i-1]
    for i in range(1, n):
        for j in range(1, n):
            cost_board[i][j] = min(
                cost_board[i-1][j], cost_board[i][j-1]) + board[i][j]
    return cost_board[n-1][n-1]


n = 5
B = [[randint(1, 10) for _ in range(n)] for _ in range(n)]
for line in B:
    print(line)
print(king(B))
