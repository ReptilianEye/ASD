from zad1testy import runtests


# Piotr Rzadkowski
# Algorytm działa tak, że wybiera element który będzie środkiem palindromu (wykorzytując to że palindrom musi miec niepatrzystą długość), a następnie sprawdza jak długi on jest dla tego elementu środkowego sprawdzając względem elementu środkowego czy pierwszy element od lewej jest taki sam jak pierwszy od prawej, drugi od lewej do drugiego od prawej itd aż do momentu kiedy nie sa równe a następnie zwraca tak policzoną długość. Element środkowy jest wybierany w ten sposób aby palindrom mógł mieć jak największa długość, czyli od środka, ponieważ wtedy ma szanse na być najdłuższym (wiadomo, że palindrom o środku na końcu lub na początku tablicy, będzie musiał mieć długość 1, a taki o pozycji n/2 będzie miał szanse mieć długość n z dokładnością do jedności). Kolejnych kandydatów wybiera aż do momentu kiedy aktualnie najdłuzsza długość palindomu jest krótsza od potencjalnej dla danego środka, (wiadomo, że jeżeli wybierzemy za środek element  na pozycji 0 to nie będzie on środkiem palindromu dłuższego niż 1, a skoro znaleźliśmy już dłuższy nie ma sensu sprawdzać dalej). Ponieważ defakto przechodzimy po wszystkich pozycjach na których może być środek najdłuższego elementu to gwaratuje nam to że znajdziemy ten który jest środkiem najdłuższego.
# Ponieważ sprawdzamy każdy środekm których jest n=długość(s) i dla każdego sprawdzamy czy on jest środkiem palindromu, która też ma złożoność liniową to ostateczna złożoność jest kwadratowa w notacji asympotycznej.


def longest_pali(s, i):
    n = len(s)
    # l = 1
    # if s[i] == "|":
    #     l -= 1
    j = 1
    while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
        j += 1
    return (j-1)


def ceasara(s):
    n = len(s)
    T_S = ["|"]*(n*2+1)
    for i in range(n):
        T_S[i*2+1] = s[i]
    s = "".join(T_S)
    n = n*2+1
    L = [0]*n
    L[0] = 0
    L[1] = 1

    # Legenda
    C = 1  # center position
    R = 2  # center right position
    i = None  # current right postion
    iMirror = 0  # current left postion

    maxLength = 1
    maxCenter = 1

    for i in range(2, n):
        iMirror = 2*C-i
        diff = R-i
        if diff > 0:
            L[i] = min(L[iMirror], diff)

        L[i] = longest_pali(s, i)
        if maxLength < L[i]:
            maxLength = L[i]
            maxCenter = i
        if L[i] + i > R:
            C = i
            R = i+L[i]

    # print(L)
    return max(L)


def ceasar(s):
    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$". # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    for i in range(1, n-1):
        # equals to i' = C - (i-C)
        P[i] = (R > i) and min(R - i, P[2*C - i])
        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return len(s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2])


runtests(ceasar, all_tests=True)
