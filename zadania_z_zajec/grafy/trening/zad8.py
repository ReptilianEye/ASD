from random import randint
from math import inf
from queue import PriorityQueue


def generate_steps():
    steps = []
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if (i, j) != (0, 0):
                steps.append((i, j))

    return steps


def sim_step(G, curr, step, vis):
    n = len(G)
    r, c = step
    new_row = curr//n + r
    new_col = curr % n + c
    new_poz = new_row*n + new_col
    if -1 < new_row < n and -1 < new_col < n and not vis[new_poz]:
        return new_poz
    return False


def generate_board(n=10):
    return [[randint(1, 5) for _ in range(n)]for _ in range(n)]


def king_journey(board):
    n = len(board)
    steps = generate_steps()
    cost = [inf]*(n*n)
    parent = [None]*(n*n)
    vis = [False]*(n*n)
    cost[0] = board[0][0]

    q = PriorityQueue()
    q.put((0, 0))
    while not q.empty():
        _, curr = q.get()
        vis[curr] = True
        for step in steps:
            res = sim_step(board, curr, step, vis)
            if res != False:
                if cost[res] > board[res//n][res % n] + cost[curr]:
                    cost[res] = board[res//n][res % n] + cost[curr]
                    parent[res] = curr
                    q.put((cost[res], res))

    return cost[n*n-1], cost, parent


board = generate_board(3)
for el in board:
    print(el)
res, cost, parent = king_journey(board)
print(res)
print(cost)
print(parent)
