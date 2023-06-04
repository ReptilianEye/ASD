# uniwesalne ujscie

def universal_sink(G):
    n = len(G)
    row = col = 0
    while row < n and col < n:
        if G[row][col] == 1:
            row += 1
        else:
            col += 1

    for i in range(n):
        if i != row and G[i][row] != 1:
            return False
    return row


G = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
]
print(universal_sink(G))
