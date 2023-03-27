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


def return_mid(p):
    s = p
    n = 0
    while s is not None:
        n += 1
        s = s.next
    s = p
    for _ in range(n//2-1):
        s = s.next
    return s


def merge_sort(p):
    if p.next is not None:
        mid = return_mid(p)
        p2 = mid.next
        mid.next = None
        p1 = merge_sort(p)
        p2 = merge_sort(p2)
        p = merge(p1, p2)
    return p


def prepare_to_sort(h, e):
    curr = h
    while curr is not e:
        curr = curr.next
    curr.next = e
    curr.next.next = None
    return h


# def copy_to_main(h, after_sort):
#     while after_sort is not None:
#         h.val = after_sort.val
#         after_sort = after_sort.next
#         h = h.next


def zad2(p, k):
    fin = Node(None)
    fin.next = p
    head = p
    end = p

    for _ in range(k):
        end = end.next
    while end is not None:
        curr = prepare_to_sort(head, end)
        after_sort = merge_sort(curr)
        copy_to_main(head, after_sort)
        head = head.next
        end = end.next


a = Node(5)
a.next = Node(2)
a.next.next = Node(3)

zad2(a, 1)
