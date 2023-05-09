from zad4testy import runtests


from collections import deque


class path:
    def __init__(self, v, len) -> None:
        self.v = v
        self.len = len


def find_shortest_length(G, s, e):
    n = len(G)
    vis = [False for _ in range(n)]
    q = deque()
    q.append(path(s, 0))
    while len(q) > 0:
        v = q.popleft()
        vis[v.v] = True
        if v.v == e:
            return v.len
        for u in G[v.v]:
            if not vis[u]:
                q.append(path(u, v.len+1))
    return None


def count_path(times_visited, path):
    for i in range(len(path)-1):
        times_visited[path[i]][path[i+1]] += 1


paths = 0


def dfs_with_limit(v, parent, end, path, G, steps_left, times_visited):
    if v == end:
        global paths
        paths += 1
        count_path(times_visited, path)
        return
    if steps_left > 0:
        for u in G[v]:
            if u != parent:
                path.append(u)
                dfs_with_limit(u, v, end, path, G,
                               steps_left - 1, times_visited)
                path.pop()


def count_edges_in_shortest_path(s, e, G, shortest):
    n = len(G)

    global paths
    paths = 0

    times_visited = [[0 for _ in range(n)] for _ in range(n)]
    dfs_with_limit(s,-1, e, [s], G, shortest, times_visited)
    for i in range(n):
        for j in range(n):
            if times_visited[i][j] == paths:
                return (i, j)
    return None


def longer(G, s, t):
    shortest = find_shortest_length(G, s, t)
    if shortest is None:
        return shortest

    return count_edges_in_shortest_path(s, t, G, shortest)


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
