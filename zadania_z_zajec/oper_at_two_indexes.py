# należy sprawdzić czy da się znaleźć w posortowanej tablicy takie dwa indexy i,j aby t[i] + t[j] = x

def find_sum_ij(t, x):
    n = len(t)
    i = 0
    j = n-1
    while i <= j:
        s = t[i]+t[j]
        if s == x:
            return (i, j)
        if s < x:
            i += 1
        else:
            j -= 1
    return False


# należy sprawdzić czy da się znaleźć w posortowanej tablicy takie indexy i,j aby t[j]-t[i]=x


def find_diff_ij(t, x):
    n = len(t)
    i = j = 0
    while j < n and i < n:
        d = t[j]-t[i]
        if d == x:
            return i, j
        if d < x:
            j += 1
        if d > x:
            i += 1
    return False
