from zad3testy import runtests
"""
Pierwszym krokiem jest przygotowanie slow. Pomyslem jest sprawdzenie czy slowo ktore zostanie odwrocone jest wczesniej leksykograficznie niz 
originalnie. Jesli tak to je odwracamy. Dzieki temu slowa rownowaczne beda takie same. Pozostaje wiec posortowac i przeliczyc ktorych jest
najwiecej.
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


def merge(t1, t2):
    t = []
    i = 0
    j = 0
    n1 = len(t1)
    n2 = len(t2)
    while i < n1 and j < n2:
        if t1[i] < t2[j]:
            t.append(t1[i])
            i += 1
        else:
            t.append(t2[j])
            j += 1
    while i < n1:
        t.append(t1[i])
        i += 1
    while j < n2:
        t.append(t2[j])
        j += 1
    return t


def merge_sort(A):
    if len(A) > 1:
        mid = len(A)//2
        t1 = merge_sort(A[:mid])
        t2 = merge_sort(A[mid:])
        A = merge(t1, t2)
    return A


def strong_string(T):
    n = len(T)
    prepare_data(T)
    T = merge_sort(T)
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
