import random
t = [random.randint(1, 50) for _ in range(8)]
# print(t)

# t = [5, 4, 3, 2, 1]


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


# wstawianie(t)
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
        if p-l+1 > 1:
            print(f"Lewy: {l}, prawy: {p}")
            m_sort(t, l, l+(p-l)//2)
            m_sort(t, l+(p-l)//2+1, p)
            merge(t, l, p)

    m_sort(T, 0, len(T)-1)
    return T


# merge_sort([1])
t = [random.randint(1, 10) for _ in range(10)]
print(t)
# t = [1, 5, 8, 2, 4, 20]
t = merge_sortV2(t)
print(t)
# t = [1, 2, 3, 4, 5, 6]
# n = len(t)
# print(t[:n//2])
# print(t[n//2:])
