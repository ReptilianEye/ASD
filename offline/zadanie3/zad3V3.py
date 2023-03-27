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


def partition_by_wage(A, l, r):

    # m_poz = find_med_wage(A, l, r)
    # A[m_poz], A[r] = A[r], A[m_poz]

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


def count_sort(A, min_v, max_v):
    n = len(A)
    C = [0]*(max_v-min_v+1)
    for i in range(n):
        C[A[i].wage - min_v] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]

    B = [0]*n
    for i in range(n-1, -1, -1):
        B[C[A[i].wage - min_v]-1] = A[i]
        C[A[i].wage - min_v] -= 1
    return B


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
    for i in range(n):
        A[i] = Word(A[i], word_wage(A[i]))
    min_v = min(A, key=lambda x: x.wage).wage
    max_v = max(A, key=lambda x: x.wage).wage
    print(min_v, max_v)
    if max_v-min_v < 1e4:
        A = count_sort(A, min_v, max_v)
    else:
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
