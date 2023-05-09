from zad4testy import runtests
from collections import deque


def longer(G, s, t):
    Q = deque()
    n = len(G)
    visited = [False for _ in range(n)]
    visited2 = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    distance[s] = 0
    visited[s] = True
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                distance[v] = distance[u] + 1
                visited[v] = True
                Q.append(v)
    if not visited[t]:
        return None
    Q.append(t)
    visited2[t] = True
    wave_counter = [0 for _ in range(distance[t]+2)]
    wave_counter[0] = 1
    ostatni_swirek = t
    current_swirek = None
    i = 1
    wave_change_counter = 0
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if distance[v] == distance[u] - 1 and not visited2[v]:
                visited2[v] = True
                wave_counter[i] += 1
                Q.append(v)
                current_swirek = v

        wave_change_counter += 1
        if wave_change_counter == wave_counter[i-1]:
            wave_change_counter = 0
            if i > 0 and wave_counter[i-1] == wave_counter[i] == 1:
                return (ostatni_swirek, current_swirek)
            i += 1
            ostatni_swirek = current_swirek
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)