from zad1testy import runtests


# Piotr Rzadkowski
# Algorytm działa tak, że wybiera element który będzie środkiem palindromu (wykorzytując to że palindrom musi miec niepatrzystą długość), a następnie sprawdza jak długi on jest dla tego elementu środkowego sprawdzając względem elementu środkowego czy pierwszy element od lewej jest taki sam jak pierwszy od prawej, drugi od lewej do drugiego od prawej itd aż do momentu kiedy nie sa równe a następnie zwraca tak policzoną długość. Element środkowy jest wybierany w ten sposób aby palindrom mógł mieć jak największa długość, czyli od środka, ponieważ wtedy ma szanse na być najdłuższym (wiadomo, że palindrom o środku na końcu lub na początku tablicy, będzie musiał mieć długość 1, a taki o pozycji n/2 będzie miał szanse mieć długość n z dokładnością do jedności). Kolejnych kandydatów wybiera aż do momentu kiedy aktualnie najdłuzsza długość palindomu jest krótsza od potencjalnej dla danego środka, (wiadomo, że jeżeli wybierzemy za środek element  na pozycji 0 to nie będzie on środkiem palindromu dłuższego niż 1, a skoro znaleźliśmy już dłuższy nie ma sensu sprawdzać dalej). Ponieważ defakto przechodzimy po wszystkich pozycjach na których może być środek najdłuższego elementu to gwaratuje nam to że znajdziemy ten który jest środkiem najdłuższego.
# Ponieważ sprawdzamy każdy środekm których jest n=długość(s) i dla każdego sprawdzamy czy on jest środkiem palindromu, która też ma złożoność liniową to ostateczna złożoność jest kwadratowa w notacji asympotycznej.

def max_palin(i, s):
    n = len(s)
    k = 0
    while i-k >= 0 and i+k < n and s[i-k] == s[i+k]:
        k += 1
    return (k-1)*2+1


def ceasar(s):
    n = len(s)
    if n == 0:
        return 0
    if n % 2 == 0:
        max_possible = n-1
        longest_palin = -1
    else:
        max_possible = n-2
        longest_palin = max_palin(n//2, s)

    while longest_palin < max_possible:
        i = max_possible//2
        longest_palin = max(max_palin(i, s), longest_palin)
        i = n-i-1
        longest_palin = max(max_palin(i, s), longest_palin)
        max_possible -= 2
    return longest_palin


runtests(ceasar, all_tests=True)
