from zad4testy import runtests


import queue


class path:
    def __init__(self, curr, parent, len) -> None:
        self.curr = curr
        self.parent = parent
        self.len = len


def find_gap(p1, p2):
    while p1 is not None and p2 is not None:
        if p2.curr == p1.curr and p2.parent.curr == p1.parent.curr:
            p1 = p1.parent
        else:
            p2 = p2.parent

    return (p1.parent.curr, p1.curr)  # bo sciezka jest od tylu spisywana


def longer(G, s, t):
    # print(G)
    n = len(G)
    q = queue.Queue()
    q.put(path(s, None, 0))
    visited = [False for _ in range(n)]
    pathA = pathB = None
    while not q.empty() and (pathA is None or pathB is None):
        v = q.get()
        if v.curr == t:
            if pathA is None:
                pathA = v
            elif pathB is None and pathA.len < v.len:
                pathB = v
        else:
            visited[v.curr] = True
            for u in G[v.curr]:
                if not visited[u]:
                    q.put(path(u, v, v.len+1))

    if pathA is None or pathB is None:
        return None
    res = find_gap(pathA, pathB)
    if res[0] > res[1]:
        res = res[::-1]
    return res


# G = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [
#     4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12], [10, 11]]

# for i in range(len(G)):
#     for el in G[i]:
#         if el > i:
#             print(i,el)
# G = [[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]
# s = 0
# t = 2
# print(longer(G, s, t))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
