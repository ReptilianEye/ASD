# znajdywanie lidera w tablicy polega na znalezieniu elementu który występuje więcej niż połowe razy
# Algorytm na znalezenie składa się z następujących kroków
# inicjujemy licznik od liczby -1
# jeśli ten licznik jest rowny -1 i jeśli nie jesteśmy na końcu tabeli to naszym nowym literem jest element na którym aktualnie stoi iterator i ustawiamy licznik na 1
# idziemy dalej i jesli kolejny element jest rowny aktualnemu liderowi zwiększamy licznik, a jeśli nie do zmniejszamy licznik
# Jeśli na koniec licznik jest większy od 0 to znaczy, że lider istnieje, jesli nie to znaczy że nie istnieje
from ... import Stack
import random


def f_leader(t):  # szuka lidera w czasie liniowym; zwraca lidera jeśli go znajdzie, w innym przypadku -1
    n = len(t)
    c_leader = -1
    cnt = 0
    for i in range(n):
        if cnt == 0:
            c_leader = t[i]
        if t[i] == c_leader:
            cnt += 1
        else:
            cnt -= 1
    if cnt == 0:
        # print(f"Lider nie istnieje")
        return -1
    else:
        cnt = 0
        for i in range(n):
            if t[i] == c_leader:
                cnt += 1
        if cnt > n//2:
            # print(f"Liderem jest {c_leader}")
            return c_leader
        else:
            # print(f"Lider nie istnieje")
            return -1


def f_leader_V2(t):  # szuka lidera w czasie liniowym; zwraca lidera jeśli go znajdzie, w innym przypadku -1
    n = len(t)
    S = Stack()
    for i in range(n):
        if S.empty():
            S.push(t[i])
        elif S.top() == t[i]:
            S.push(t[i])
        else:
            S.pop()
    if S.empty():
        # print(f"Lider nie istnieje")
        return -1
    else:
        c_leader = S.top()
        cnt = 0
        for i in range(n):
            if t[i] == c_leader:
                cnt += 1
        if cnt > n//2:
            return c_leader
            # print(f"Liderem jest {kand}")
        else:
            return -1
            # print(f"Lider nie istnieje")


def testing(n=20, it=10e4):
    err = False
    for i in range(10000):
        t = [1 for _ in range(random.randint(7, 12))]
        while len(t) < n:
            t.append(random.randint(2, 10))
        random.shuffle(t)
        if f_leader(t) != f_leader_V2(t):
            err = True
            print(f"Bład dla {i}: {t}")
    if not err:
        print("Wszystko działa!")
