# dana jest tablica krotek które oznaczają początek i koniec odcinka. Wiadomo, że żaden odcinek nie może sie zaczynać ani kończyć w tym samym miejscu co inny
# należy znaleźć taki odcinek który zawiera w sobie jak najwięcej innych odcinków

# Algorytm:
# Algorytm jest oparty na policzniu ile odcinków sie zaczeło od pewnego indexu i ile się zakończyło do tego indexu.
# Pierwszym krokiem jest posortowanie tablicy wzgledem indexu początkowego. Następnie zaznaczamy "na osi" punkty gdzie dane odcinki się zaczynają i kończą, tak aby móc potem przejechać po tej osi i stworzyć dwie tablice które oznaczają ile odcinków sie zaczyna i kończy patrząc od danego indexu.
# Ostatnim krokiem jest policzenie dla każdego odcinka działania skończone[koniec odcinka]-rozpoczęte[poczatek odcinka]. Po zrobieniu tego działania widzimy ile odcinków które nie zaczęly się przed danym skończyły sie przed jego końcem, a to oznacza, że musiał się zacząć po nim (czyli jest w jego środku)
# Aby nie tworzyc gigantycznej tablicy jeśli każdy odcinek zaczyna się zawsze od np 100, przesuwamy indexy o ten index początku odcinka najbardziej na lewo, czego skutkiem oszczędzamy pamieć.
def segments(t):  # O(n^2)
    starting_index = min(t, key=lambda x: x[0])[0]
    n = max(t, key=lambda x: x[1])[1]+1-starting_index
    started = [0 for _ in range(n)]
    ended = started[:]
    for odc in t:
        i = odc[0]-starting_index
        j = odc[1]-starting_index
        while i < n:
            started[i] += 1
            i += 1
        while j < n:
            ended[j] += 1
            j += 1
    max_covers = -1
    max_covers_seg = ()
    for odc in t:
        covers = ended[odc[1]-starting_index]-started[odc[0]-starting_index]
        if max_covers < covers:
            max_covers = covers
            max_covers_seg = odc
    print(max_covers_seg, max_covers)


def segmentsV2(t):  # O(nlogn) + dodatkowa struktura danych
    t.sort(key=lambda x: x[0])
    starting_index = t[0][0]
    n = max(t, key=lambda x: x[1])[1]+1-starting_index
    axis = ["" for _ in range(n)]
    for odc in t:
        axis[odc[0]-starting_index] = "S"
        axis[odc[1]-starting_index] = "E"

    started = [0 for _ in range(n)]
    ended = started[:]

    already_started = 0
    already_ended = 0
    for i in range(n):
        if axis[i] == "S":
            already_started += 1
        if axis[i] == "E":
            already_ended += 1
        started[i] = already_started
        ended[i] = already_ended

    max_covers = -1
    max_covers_seg = ()
    for odc in t:
        covers = ended[odc[1]-starting_index]-started[odc[0]-starting_index]
        if max_covers < covers:
            max_covers = covers
            max_covers_seg = odc
    print(max_covers_seg, max_covers)


odcinki = [(0, 2), (1, 7), (4, 6), (3, 5), (9, 11),
           (10, 13), (8, 12)]  # odpowiedz: (1,7), 2
# odcinki = [(0, 5), (1, 2), (3, 4), (6, 13), (7, 8),
#    (9, 10), (11, 12)]  # odpowiedz: (6,13), 3
segmentsV2(odcinki)
