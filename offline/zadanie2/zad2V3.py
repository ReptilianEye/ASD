from zad2testy import runtests


def better_pivot(A, p, r):
    avg = round(sum(A[p:r+1])/(r-p+1))
    best = p
    gap = abs(avg-A[p])
    for i in range(p, r+1):
        curr_gap = abs(avg-A[i])
        if gap > curr_gap:
            gap = curr_gap
            best = i
    return best


def find_med(A, p, r):
    if p == r or p+1 == r:
        return r
    i = 0
    temp = []
    while i < 3:
        temp.append(A[r-i])
        i += 1
    median = sum(temp)-max(temp)-min(temp)
    i = 0
    while temp[i] != median:
        i += 1
    return r-i


def partition(A: list, p: int, r: int):
    # m = find_med(A, p, r)   #0.54 sek
    # A[m], A[r] = A[r], A[m]
    # b = better_pivot(A, p, r) #1.54 sek
    # A[b], A[r] = A[r], A[b]

    # 0.7 sek
    x = A[r]
    i = p-1

    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def snow(t):
    n = len(t)
    p = 0
    r = n-1
    while p <= r:
        q = partition(t, p, r)
        if t[q]-q == 0:
            break
        if t[q]-q > 0:
            p = q+1
        else:
            r = q-1
    i = 0
    while t[q-i]-(q-i) < 0:
        i += 1
    # print(i)
    q = q-i
    # q-=1 #prawdopodobnie mozna by tak ale jest to za bardzo ryzykowne na razie
    s = 0

    for i in range(min(q+1, n)):
        s += t[i]-i
    return s


# A = list(range(10))
# print(t)

# print(snow(A))
# print(q)
# n = int(10e6)
# t = [1 for _ in range(n)]
# s = 0
# for i in range(n):
#     s += t[i]
# print(s)
runtests(snow, all_tests=True)
# a = [1, 2, 3, 4]
# print(a[1:3])
# print(sum(a[0:3]))
