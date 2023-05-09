from zad4testy import runtests


from collections import deque


def shortest_and_indegrees(G, s, e):
    n = len(G)
    vis = [False for _ in range(n)]
    indeegres = [0 for _ in range(n)]
    q = deque()
    shortest = None
    q.append((s, 0))
    while len(q) > 0:
        v, length = q.popleft()
        vis[v] = True
        for u in G[v]:
            if not vis[u]:
                if u != e:
                    q.append((u, length+1))
                if u == e and shortest is None:
                    shortest = length+1
            indeegres[u] += 1
    for u in G[e]:
        indeegres[u] += 1
    return shortest, indeegres


def count_path(G, times_visited, path):
    for i in range(len(path)-1):
        times_visited[path[i]][G[path[i]].index(path[i+1])] += 1


paths = 0


def dfs_with_limit(v, parent, end, path, G, steps_left, times_visited):
    if v == end:
        global paths
        paths += 1
        count_path(G, times_visited, path)
        return
    if steps_left > 0:
        for u in G[v]:
            if u != parent:
                path.append(u)
                dfs_with_limit(u, v, end, path, G,
                               steps_left - 1, times_visited)
                path.pop()


def count_edges_in_shortest_path(s, e, G, shortest, indeegres):
    n = len(G)

    global paths
    paths = 0

    paths_through_nodes = [0 for _ in range(n)]

    dfs_with_limit(s, -1, e, [s], G, shortest, indeegres, paths_through_nodes)
    for v in range(n):
        if times_visited[v][j] == paths:
            return (v, G[v][j])
    return None


def longer(G, s, t):
    shortest, indeegres = shortest_and_indegrees(G, s, t)
    if shortest is None:
        return shortest

    return count_edges_in_shortest_path(s, t, G, shortest)


# G = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [
#     4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12], [10, 11]]
G = [[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]

for i in range(len(G)):
    for el in G[i]:
        if el > i:
            print(i, el)
s = 0
t = 2
for i in range(len(G)):
    for el in G[i]:
        if el > i:
            print(i, el)

print(longer(G, s, t))


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(longer, all_tests=True)
