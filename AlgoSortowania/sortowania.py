from copy import deepcopy
import string
from struktury import Node
import random
t = [random.randint(1, 50) for _ in range(8)]


def testerka_sort(n=100, it=1000):
    for _ in range(it):
        t = [random.randint(1, n*2) for _ in range(n)]
        t_rob = t[:]
        blad = False
        if sorted(t) != wstawianie(t_rob):
            print(f"Bład dla {t}")
            blad = True
    if not blad:
        print("Wszystko w porządku")


def babelkowe(t):
    n = len(t)
    i = 1
    while i < n:
        j = 1
        while j < n-i+1:
            if t[j-1] > t[j]:
                t[j-1], t[j] = t[j], t[j-1]
            j += 1
        i += 1
    return t


# babelkowe(t)
def wybieranie(t):
    n = len(t)
    i = 0
    while i < n-1:
        j = i+1
        _min = i
        while j < n:
            if t[_min] > t[j]:
                _min = j
            j += 1
        t[i], t[_min] = t[_min], t[i]
        i += 1
    return t
# wybieranie(t)


def wstawianie(t):
    n = len(t)
    i = 1
    while i < n:
        j = 0
        while j < i:
            if t[i] < t[j]:
                t.insert(j, t.pop(i))
                break
            j += 1
        i += 1
    return t


def merge_sort(T):
    def merge(t1, t2):
        n1 = len(t1)
        n2 = len(t2)
        t = [-1 for _ in range(n1+n2)]

        i = j = 0
        k = 0
        while i < n1 and j < n2:
            if t1[i] <= t2[j]:
                t[k] = t1[i]
                i += 1
            else:
                t[k] = t2[j]
                j += 1
            k += 1
        while i < n1:
            t[k] = t1[i]
            i += 1
            k += 1
        while j < n2:
            t[k] = t2[j]
            j += 1
            k += 1
        return t

    def m_sort(t):
        n = len(t)
        if n == 1:
            return t
        t1 = m_sort(t[:n//2])
        t2 = m_sort(t[n//2:])
        return merge(t1, t2)
    return m_sort(T)


def merge_sortV2(T):
    def merge(t, l, p):
        n = p-l+1
        t_rob = [-1 for _ in range(n)]
        l1 = l
        l2 = p1 = l+(p-l)//2+1
        p2 = p+1
        i = 0
        while l1 < p1 and l2 < p2:
            if t[l1] <= t[l2]:
                t_rob[i] = t[l1]
                l1 += 1
            else:
                t_rob[i] = t[l2]
                l2 += 1
            i += 1
        while l1 < p1:
            t_rob[i] = t[l1]
            l1 += 1
            i += 1
        while l2 < p2:
            t_rob[i] = t[l2]
            l2 += 1
            i += 1
        for i in range(n):
            t[l+i] = t_rob[i]

    def m_sort(t, l, p):
        if p > l:
            # print(f"Lewy: {l}, prawy: {p}")
            mid = l+(p-l)//2
            m_sort(t, l, mid)
            m_sort(t, mid+1, p)
            merge(t, l, p)

    m_sort(T, 0, len(T)-1)
    return T


def merge_sort_dyn(h):  # dla listy dynamicznej jednokierunkowej z wartownikiem
    def merge(h1, h2):
        h = Node()
        h_fin = h
        h1 = h1.next  # wykorzystuje że listy są z wartownikiem
        h2 = h2.next
        while h1 is not None and h2 is not None:
            if h1.val < h2.val:
                h.next = h1
                h1 = h1.next
            else:
                h.next = h2
                h2 = h2.next
            h = h.next
        if h1 is not None:
            h.next = h1
        else:
            h.next = h2
        return h_fin

    def m_sort(h):
        # nie wiem na razie
        pass


def heap_sort(T):
    def left(i): return i*2+1
    def right(i): return i*2+2
    def parent(i): return (i-1)//2

    def heapify(i, n, t):
        l = left(i)
        r = right(i)
        max_ind = i

        if l < n and t[max_ind] < t[l]:
            max_ind = l
        if r < n and t[max_ind] < t[r]:
            max_ind = r
        if max_ind != i:
            t[i], t[max_ind] = t[max_ind], t[i]
            heapify(max_ind, n, t)

    def build_heap(t):
        n = len(t)
        for i in range(parent(n-1), -1, -1):
            heapify(i, n, t)
        return t

    def h_sort(t):
        n = len(t)
        build_heap(t)
        for i in range(n-1, 0, -1):
            t[0], t[i] = t[i], t[0]
            heapify(0, i, t)
        return t
    return h_sort(t)


def quick_sort(t, classic=True):
    def partition(A, l, r):
        x = A[r]
        i = l-1
        for j in range(l, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1

    # bardzo mocny, bo wykonuje mniej operacji niż heap_sort. Wadą jest złożoność kwadratowa w pesymistycznym przypadku
    def classic_quick_sort(A, l, r):
        if l < r:
            q = partition(A, l, r)
            classic_quick_sort(A, l, q-1)
            classic_quick_sort(A, q+1, r)
    # wariacja klasycznego. Benefitem jest zredukowana głebokość rekursji, na rzecz uzycia pętli

    def rec_depth_quick_sort(A, l, r):
        while l < r:
            q = partition(A, l, r)
            if q-l < r-q:
                rec_depth_quick_sort(A, l, q-1)
                l = q+1
            else:
                rec_depth_quick_sort(A, q+1, r)
                r = q-1
    if classic:
        classic_quick_sort(t, 0, len(t)-1)
    else:
        rec_depth_quick_sort(t, 0, len(t)-1)


# dobry jeśli mamy dane, że liczby są z pewnego zakresu [a,b]. Wtedy ma złożoność O(n)
def count_sort(t, a=0, b=10e3, stable=True):
    def prepare_counts(t, a, b):
        n = len(t)
        # a = min(T)
        # b = max(T)
        k = b-a+1
        counts = [0] * k
        for i in range(n):
            counts[t[i]-a] += 1
        return counts

    def c_sort_unstable(t, a, b):
        n = len(t)
        counts = prepare_counts(t, a, b)
        res = [0]*n
        j = 0
        i = 0
        while True:
            while counts[j] == 0:
                j += 1
            res[i] = j
            counts[j] -= 1
            i += 1
            if i == n:
                return res

    def c_sort_stable(t, a, b):
        counts = prepare_counts(t, a, b)
        n = len(t)
        k = len(counts)
        for i in range(1, k):  # cumulative sum
            counts[i] += counts[i-1]
        res = [0]*n
        for i in range(n-1, -1, -1):
            res[counts[t[i]]-1] = t[i]
            counts[t[i]] -= 1
        return res
    b += 1
    if stable:
        return c_sort_stable(t, a, b)
    else:
        return c_sort_unstable(t, a, b)


def test_c_sort(a=0, b=10e2, n=10e4, it=10e4):
    err = False
    a = int(a)
    b = int(b)
    n = int(n)
    it = int(it)
    for i in range(int(it)):
        t = [random.randint(a, b) for _ in range(n)]
        stable = count_sort(t, a, b, True)
        unstable = count_sort(t, a, b, False)
        t.sort()
        if stable != unstable or stable != t:
            print(f"Bład dla {i}")
            err = True
        else:
            print(f"Dobrze dla {i}")

    if not err:
        print("Bez błedów")


alfabeth = string.ascii_lowercase
# na przykladzie sortowania slow tej samej dlugosci


def radix_sort(A):
    def get_index(char):
        t = ord(char) - ord(alfabeth[0])
        return t

    def csort_by_letters(A, col):
        n = len(A)
        letters = len(alfabeth)
        Counts = [0]*letters
        for el in A:
            Counts[get_index(el[col])] += 1
        for i in range(1, letters):
            Counts[i] += Counts[i-1]
        Result = [0]*n
        for i in range(n-1, -1, -1):
            p = get_index(A[i][col])
            Result[Counts[p]-1] = A[i]
            Counts[p] -= 1
        return Result
    def radix_words(A):
        words_length = len(A[0])
        for i in range(words_length-1, -1, -1):
            A = csort_by_letters(A, i)
        return A

    def get_digit_index(num,col):
        pass
    def csort_by_numbers(A,col):
        n=len(A)
        digits = 10
        C = [0]*digits
        for el in A:
            C[el%col]

    def radix_numbers(A):
        numbers_length = len(A[0])
        for i in range(numbers_length-1, -1, -1):
            A = csort_by_numbers(A, i)
        return A


def test_radix(n=100, w_length=100, tries=100):
    err = False
    for _ in range(tries):
        l = []
        for _ in range(n):
            s = ""
            for _ in range(w_length):
                s = s+alfabeth[random.randint(0, len(alfabeth)-1)]
            l.append(s)
        prime = deepcopy(l)
        prime.sort()
        res = radix_sort(l)
        if prime != res:
            print("BLAAAD")
            err = True
    if not err:
        print("Success!!!")


test_radix()
