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


def right(i): return i*2+1
def left(i): return i*2+2
def parent(i): return (i-1)//2


def heapify_len(A, i, n):
    max_ind = i
    l = left(i)
    r = right(i)
    if l < n and len(A[l].word) > len(A[max_ind].word):
        max_ind = l
    if r < n and len(A[r].word) > len(A[max_ind].word):
        max_ind = r
    if max_ind != i:
        A[max_ind], A[i] = A[i], A[max_ind]
        heapify_len(A, max_ind, n)


def heapify_wage(A, i, n):
    max_ind = i
    l = left(i)
    r = right(i)
    if l < n and A[l].wage > A[max_ind].wage:
        max_ind = l
    if r < n and A[r].wage > A[max_ind].wage:
        max_ind = r
    if max_ind != i:
        A[max_ind], A[i] = A[i], A[max_ind]
        heapify_wage(A, max_ind, n)


def build_heap(A, l, r, heapify):
    for i in range(parent(r), l-1, -1):
        heapify(A, i, r)


def sort_by_length(A, l, r):
    build_heap(A, l, r, heapify_len)
    for i in range(r, l-1, -1):
        A[l], A[i] = A[i], A[l]
        heapify_len(A, l, i)


def sort_by_wage(A, l, r):
    build_heap(A, l, r, heapify_wage)

    for i in range(r, l-1, -1):
        A[l], A[i] = A[i], A[l]
        heapify_wage(A, l, i)


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


def find_strongestV2(A, l, r):
    # checked = [False for _ in range(r-l+1)]
    strongest = -1
    i = l
    # print(l, r)
    # print_range(A, l, r)

    while i <= r:
        if A[i] is not None:
            curr_strong = 1
            # checked[i-r] = True
            # curr_str = A[i].word
            # curr_wage=A[i].wage
            curr = A[i]
            A[i] = None
            j = i+1
            while j <= r:
                if A[j] is not None:
                    if len(curr.word) != len(A[j].word):
                        break
                    if (A[j].word == curr.word or A[j].word == curr.word[::-1]):
                        curr_strong += 1
                        A[j] = None
                        # checked[j-r] = True
                j += 1
            strongest = max(strongest, curr_strong)
        i += 1
    return strongest


def print_range(A, l, p):
    for i in range(l, p+1):
        print(A[i].word, A[i].wage)
    print()
    print()


def strong_string(T):
    n = len(T)
    wages = [0]*n
    for i in range(n):
        T[i] = Word(T[i], word_wage(T[i]))
        # wages[i] = word_wage(T[i])
    # return 0
    sort_by_wage(T, 0, n-1)
    # return 0;
    # print("posortowano")
    # sort_by_length(T, 0, n-1)

    strongest = 1
    i = 0
    while i < n:
        j = i+1
        while j < n and T[i].wage == T[j].wage:
            j += 1
        if j-1-i > strongest:
            # sort_by_wage(T, i, j-1)
            # sort_by_length(T, i, j-1)
            # print_range(T, i, j-1)
            if j-i > strongest:
                # curr_strongest = find_strongest(T, i, j-1)
                curr_strongest = find_strongestV2(T, i, j-1)

                strongest = max(curr_strongest, strongest)
        i = j
    return strongest


T = ["pies", "mysz", "kot", "kogut", "tok",
     "seip", "kot", "zzz", "AAAA", "yzd"]

# print(strong_string(T))

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)
