import random
from zad2testy import runtests


def left(i): return i*2+1
def right(i): return i*2+2
def parent(i): return (i-1)//2


def heapify(t, i, n):
    l = left(i)
    r = right(i)

    max_ind = i
    if l < n and t[max_ind] < t[l]:
        max_ind = l
    if r < n and t[max_ind] < t[r]:
        max_ind = r
    if max_ind != i:
        t[i], t[max_ind] = t[max_ind], t[i]
        heapify(t, max_ind, n)


def build_heap(t):
    n = len(t)
    for i in range(parent(n-1), -1, -1):
        heapify(t, i, n)


# def calc_sum(t, i):
#     s = 0
#     for round in range(i):
#         s += t[round]-round
#     return s


def snow(t):
    build_heap(t)
    n = len(t)
    s = 0
    round = 0
    # round=(n-1)-i tak też można napisać ale jest chyba trudniej napisane
    for i in range(n-1, 0, -1):
        t[0], t[i] = t[i], t[0]

        if t[i]-round <= 0:
            break

        s += t[i]-round
        round += 1

        heapify(t, 0, i)
    # t = heap_sort(t)
    # # t = sorted(t, reverse=True)
    
    # i = 0
    # while t[i] - i > 0:
    #     i += 1
    # sum = calc_sum(t, i)
    return s


# S = [1, 7, 3, 4, 1]
# print(snow(S))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=False)
