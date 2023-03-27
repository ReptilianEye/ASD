import random
from zad3testy import runtests
"""
Niech wagą słowa jest suma wartosci funkcji ord() dla kazdej litery. Mozna zauważyć, że wagi słow równoważnych muszą być sobie równe, tak samo jak długości tych słów. Zadanie więc sprawdza się do posortowania tablicy względem wag a następnie względem długości. Po takich operacjach wyrazy równoważne mogą być tylko do momentu, aż nie zgadza się jedna z dwóch wyżej wymienionych cech. W tak okrojonym przedziale wystarczy porównać ze sobą wyrazy w odpowiedni sposób i otrzymujemy wynik.

"""


def print_range(A, l, p):
    for i in range(l, p+1):
        print(A[i].word, A[i].wage)
    print()
    print()


def prepare_data(A):
    n = len(A)
    for i in range(n):
        if A[i][::-1] < A[i]:
            A[i] = A[i][::-1]


def partition(A, l, r):
    # better_med(A, l, r)
    x = A[r]
    i = l-1
    for j in range(l, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


# def quick_sort(A, l, r):
#     if l < r:
#         q = partition(A, l, r)
#         quick_sort(A, l, q-1)
#         quick_sort(A, q+1, r)


def quick_sort_rs(A, l, r):
    while l < r:
        q = partition(A, l, r)
        if q-l < r-q:
            quick_sort_rs(A, l, q-1)
            l = q+1
        else:
            quick_sort_rs(A, q+1, r)
            r = q-1


def strong_string(T):
    n = len(T)
    prepare_data(T)
    # A = [random.randint(0, 100) for _ in range(n)]
    A = [0 for _ in range(n)]
    quick_sort_rs(A, 0, n-1)
    strongest = 1
    i = 0
    while i < n:
        curr = 1
        j = i+1
        while j < n and T[i] == T[j]:
            j += 1
            curr += 1
        if strongest < curr:
            strongest = curr
        i = j
    return strongest


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)
