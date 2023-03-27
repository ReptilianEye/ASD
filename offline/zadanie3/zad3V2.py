from zad3testy import runtests
"""
Niech wagą słowa jest suma wartosci funkcji ord() dla kazdej litery. Mozna zauważyć, że wagi słow równoważnych muszą być sobie równe, tak samo jak długości tych słów. Zadanie więc sprawdza się do posortowania tablicy względem wag a następnie względem długości. Po takich operacjach wyrazy równoważne mogą być tylko do momentu, aż nie zgadza się jedna z dwóch wyżej wymienionych cech. W tak okrojonym przedziale wystarczy porównać ze sobą wyrazy w odpowiedni sposób i otrzymujemy wynik.

"""


class Word():
    def __init__(self, word, wage) -> None:
        self.word = word
        self.wage = wage


def word_wage(wage):
    s = 0
    for char in wage:
        s += ord(char)
    return s


# def right(i): return i*2+1
# def left(i): return i*2+2
# def parent(i): return (i-1)//2


# def heapify_len(A, i, n):
#     max_ind = i
#     l = left(i)
#     r = right(i)
#     if l < n and len(A[l].word) > len(A[max_ind].word):
#         max_ind = l
#     if r < n and len(A[r].word) > len(A[max_ind].word):
#         max_ind = r
#     if max_ind != i:
#         A[max_ind], A[i] = A[i], A[max_ind]
#         heapify_len(A, max_ind, n)


# def heapify_wage(A, i, n):
#     max_ind = i
#     l = left(i)
#     r = right(i)
#     if l < n and A[l].wage > A[max_ind].wage:
#         max_ind = l
#     if r < n and A[r].wage > A[max_ind].wage:
#         max_ind = r
#     if max_ind != i:
#         A[max_ind], A[i] = A[i], A[max_ind]
#         heapify_wage(A, max_ind, n)


# def build_heap(A, l, r, heapify):
#     for i in range(parent(r), l-1, -1):
#         heapify(A, i, r)


# def sort_by_length(A, l, r):
#     build_heap(A, l, r, heapify_len)
#     for i in range(r, l-1, -1):
#         A[l], A[i] = A[i], A[l]
#         heapify_len(A, l, i)


# def sort_by_wage(A, l, r):
#     build_heap(A, l, r, heapify_wage)

#     for i in range(r, l-1, -1):
#         A[l], A[i] = A[i], A[l]
#         heapify_wage(A, l, i)
def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(1, n-i):
            # if A[j-1].wage > A[j].wage:
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]


def find_med_wage(A, l, r):
    n = 5
    if r-l < n+1:
        return r
    temp = []
    for i in range(r-n, r):
        temp.append(A[i].wage)
    bubble_sort(temp)
    m = temp[len(temp)//2]
    m_poz = r-n
    while A[m_poz].wage != m:
        m_poz += 1
    return m_poz


def partition_by_wage(A, l, r):

    m_poz = find_med_wage(A, l, r)
    A[m_poz], A[r] = A[r], A[m_poz]

    x = A[r].wage
    i = l-1
    for j in range(l, r):
        if A[j].wage <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    # print(f"pivot: {x}")
    # print_range(A,l,r)
    return i+1


def partition_by_len(A, l, r):

    x = len(A[r].word)
    i = l-1
    for j in range(l, r):
        if len(A[j].word) <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    # print(f"pivot: {x}")
    # print_range(A,l,r)
    return i+1


def sort_by_wage_qs(A, l, r):
    if l < r:
        q = partition_by_wage(A, l, r)
        sort_by_wage_qs(A, l, q-1)
        sort_by_wage_qs(A, q+1, r)


def qs_sort_rec_save(A, l, r, partition):
    while l < r:
        q = partition(A, l, r)
        if q-l < r-q:
            qs_sort_rec_save(A, l, q-1, partition)
            # print_range(A,l,q-1)
            l = q+1
        else:
            qs_sort_rec_save(A, q+1, r, partition)
            # print_range(A,q+1,r)
            r = q-1


def find_strongest(A, l, r):
    checked = [False for _ in range(r-l+1)]
    strongest = -1
    i = l
    # print(l, r)
    # print_range(A, l, r)

    while i <= r:
        curr_strong = 1
        checked[i-r] = True
        # curr_str = A[i].word
        # curr_wage=A[i].wage
        curr = A[i]

        j = i+1
        while j <= r:
            if len(curr.word) != len(A[j].word):
                break
            if not checked[j-r] and (A[j].word == curr.word or A[j].word == curr.word[::-1]):
                curr_strong += 1
                checked[j-r] = True
            j += 1
        strongest = max(strongest, curr_strong)
        i += 1
        while i <= r and checked[i-r]:
            i += 1
    return strongest


def print_range(A, l, p):
    for i in range(l, p+1):
        print(A[i].word, A[i].wage)
    print()
    print()


def strong_string(A):
    n = len(A)
    # s = []
    # for i in range(n):
    #     s.append(word_wage(A[i]))
    # s = list(set(s))
    # s.sort()
    # print(s)
    # return
    for i in range(n):
        A[i] = Word(A[i], word_wage(A[i]))

    # sort_by_wage(T, 0, n-1)
    # sort_by_length(T, 0, n-1)
    qs_sort_rec_save(A, 0, n-1, partition_by_wage)
    # print_range(A, 0, n-1)
    strongest = 1
    i = 0
    while i < n:
        j = i+1
        while j < n and A[i].wage == A[j].wage:
            j += 1
        if j-1-i > strongest:
            # sort_by_wage(T, i, j-1)
            # qs_sort_rec_save(A, i, j-1,partition_by_len)
            # print_range(T, i, j-1)
            if j-i > strongest:
                curr_strongest = find_strongest(A, i, j-1)
                strongest = max(curr_strongest, strongest)
        i = j
    return strongest


# print(strong_string(T))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)
