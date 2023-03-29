from copy import deepcopy


def partition(A, l, r):
    x = A[r]
    i = l-1
    for j in range(l, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def k_biggest(A, col):
    n = len(A)
    copy = [A[row][col] for row in range(n)]
    l = 0
    r = n-1
    while True:
        q = partition(copy, l, r)
        if q == col:
            break
        if q > col:
            r = q-1
        else:
            r = q+1
    for i in range(n):
        A[i][col] = copy[i]


def zad1(T):
    n = len(T)
    for col in range(n):
        k_biggest(T, col)

    for row in T:
        for el in row:
            print(el, end=" ")
        print()

# import random

# n=5
# T=[[random.randint(0,20) for _ in range(n)] for _ in range(n)]

# zad1(T)


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


def get_k_el(p, k):
    new_p = deepcopy(p)
    curr = new_p
    i = 0
    while curr is not None and i < k-1:
        curr = curr.next
        i += 1
    if curr is None:
        return -1, None
    next_after = curr.next
    curr.next = None
    return new_p, next_after


def merge(p1, p2):
    p = Node(None)
    curr = p
    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next
        p = p.next
    if p1 is not None:
        p.next = p1
    else:
        p.next = p2
    return curr.next


def split(p, p1, p2):
    f = True
    while p:
        if f:
            p1.next = p
            p1 = p1.next
        else:
            p2.next = p
            p2 = p2.next
        p = p.next
        f = not f
    if p1 is not None:
        p1.next = None
    if p2 is not None:
        p2.next = None


def merge_sort(p):
    if p is not None and p.next is not None:
        p1 = Node(None)
        p2 = Node(None)
        split(p, p1, p2)
        p1 = merge_sort(p1.next)
        p2 = merge_sort(p2.next)
        p = merge(p1, p2)
    return p


def zad2(p, k):
    first = Node(None)
    first.next = p
    p = first
    while True:
        cutted, next_after = get_k_el(p.next, k)
        if cutted == -1:
            break
        cutted_sorted = merge_sort(cutted)
        p.next = cutted_sorted
        temp = p.next
        while temp.next is not None:
            temp = temp.next
        temp.next = next_after
        p = p.next
    first = first.next
    while first:
        print(first.val)
        first = first.next


a = Node(2)
a.next = Node(1)
a.next.next = Node(4)
a.next.next.next = Node(3)


zad2(a, 2)
