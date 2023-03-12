# Dana jest tablica zawierająca n liczb z zakresu[0...n^2-1]. Napisz algorytm, który posortuje taką
# tablicę w czasie O(n).

# Pomysł na algorytm:
# Algorytm jest oparty na radix sort. Liczby z takiego zakresu można przedstawić w jako liczbę ( % n^2, % n). Posortowanie takiej tablicy będzie więc posrtowaniem tablicy liczb po %n a potem po %n^2. Ponieważ mamy dwa sortowania które mozna zrobić w czasie O(n) algorytm ma złożoność liniową.


from random import randint


def solve(t):
    def posortuj_modk(t, k):
        n = len(t)
        counts = [0]*k
        for i in range(n):
            counts[t[i] % k] += 1
        for i in range(1, k):
            counts[i] += counts[i-1]
        res = [0]*n
        for i in range(n-1, -1, -1):
            res[counts[t[i] % k]-1] = t[i]
            counts[t[i] % k] -= 1
        return res

    t = posortuj_modk(t, len(t))
    t = posortuj_modk(t, len(t)**2)
    return t


n = 30
t = [randint(0, n*n-1) for _ in range(n)]
print(t)

t = solve(t)
print(t)
