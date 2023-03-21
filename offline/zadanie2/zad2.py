from zad2testy import runtests
"""
Piotr Rzadkowski
Algorytm opiera się na dwóch założeniach: rozwiązaniem jest suma k najwiekszych pól i kolejność wyboru pól nie ma znaczenia. Wynikają one z tego, że w każdej rundzie każde pole "topnieje" o dokładnie tyle samo, więc największe pola zawsze pozostaną największe (tj. najbardziej opłacalne do zebrania).
Oczekiwany wynik można przedstawić jako sume: p1+(p2-1)+...+(pk-k)=p0+p1+...pk-(0+1+...+k). (p0...pk to wartości pól) Widać z tego, że dobór p0,p2...pk do sumy nie ma wpływu na poprawność.

Stąd wynika wzór, że po posortowaniu malejąco tablicy z polami to wartości "opłacalne" muszą spełniać warunek t[i] > i.
Jeśli t[i] == i to pole nie ma znaczenia do wyniku, a dla t[i] < i wzięcie tego będzie wyborem nieoptymalnym.

Sam algorytm opiera się na funkcji partition, której celem jest znalezienie takiej liczby, dla której t[i]==i. Robi to aż do momentu kiedy znajdzie, lub szukany przedział będzie pusty. Jeśli t[i]>i to wywołujemy partition() dla prawej strony, w innym przypadku - dla lewej. 
"""


def find_med(A: list, p: int, r: int):
    if p == r or p+1 == r:
        return r
    a = A[r]
    b = A[r-1]
    c = A[r-2]
    median = a+b+c - max(a, b, c)-min(a, b, c)
    for i in range(3):
        if A[r-i] == median:
            return r-i


def partition(A: list, p: int, r: int):
    m = find_med(A, p, r)  # 0.54 sek
    A[m], A[r] = A[r], A[m]
    x = A[r]
    i = p-1

    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def snow(t: list):
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
    q = q-i
    # q-=1 #prawdopodobnie mozna by tak ale jest to za bardzo ryzykowne na razie
    s = 0

    for i in range(min(q+1, n)):
        s += t[i]-i
    return s


runtests(snow, all_tests=True)
