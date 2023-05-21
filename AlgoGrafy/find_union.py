class Node:
    def __init__(self, val) -> None:
        self.parent = self
        self.rank = 0
        self.val = val


def findset(x):
    if x.parent is not x:
        x.parent = findset(x.parent)
    return x.parent


def union(x, y):
    x = findset(x)
    y = findset(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
