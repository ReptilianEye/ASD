## ASD-EX
1.	Sprawdzić czy graf jest dwudzielny
2.	Znaleźć wszystkie spójne składowe
3.	Znany operator linii komórkowych splajtuje i usuwa swoje urządzenia, ze względów technologicznych urządzenia należy usuwać pojedynczo, a graf ma pozostać spójny
4.	Graf nieskierowany o n wierzchołkach; zaproponować algorytm który stwierdza czy w Grafie jest cykl który składa się z dokładnie 4 wierzchołków
5.	 Uniwersalne ujście
6.	BFS tak, aby znajdował najkrótszą ścieżke (z wagami) i następnie żeby dało się wypisać (bez Dijkstry)
7.	Graf z parami różnymi wagami z zakresu 1-|E|, sprawdzić czy dla danych wierzchołków x,y istnieje ścieżka z x do y po której przechodzimy po krawędziach o coraz mniejszych wagach  
8.	Szachownica o wymiarach NxN, każde pole [i][j] ma koszt od 1-5, w lewym górnym roku szachownicy stoi król, który ma przejść do prawego dolnego przechodząc po polach o minimalnym sumarycznym koszcie
9.	Ścieżka Hamiltona w DAG’u
10.	Wierzchołek v w grafie skierowanym nazywamy tzw. dobrym początkiem, jeśli każdy inny wierzchołek można osiągnąć ścieżką skierowaną wychodzącą z v. Podać algorytm który dla podanego grafu stwierdza czy G posiada dobry początek
11.	Przewoźnik chce przewieść grupę k turystów z miasta A do miasta B, między tymi miastami jest wiele miast i pomiędzy tymi miastami jeżdżą autobusy o różnej pojemności mamy graf połączeń w postaci trójek [x,y,c] gdzie x,y – miasta; c – pojemność autobusu na tej trasie. Przewoźnik musi wyznaczyć wspólną trasę dla wszystkich turystów, musi w związku z tym ich podzielić na grupki tak, żeby każda grupka mogła przebyć trasę bez rozdzielania się, podaj algorytm który wylicza na ile grupek trzeba podzielić ich 
12.	Znaleźć cykl Eulera i go zwrócić
13.	Algocja leży na wielkiej pustyni i składa się z miast, oraz oaz połączonymi drogami, każde miasto jest otoczone murem i ma tylko 2 bramy, północną i południową. Z każdej bramy prowadzi dokładnie 1 droga do 1 oazy, do daniej oazy może dochodzić dowolnie wiele dróg i oazy mogą był połączone drogami między sobą. Prawo algocji wymaga że jeśli ktoś wjechał do miasta jedną bramą to musi wyjechać drugą. Szach Algocji postanowił wysłać gońca, który w każdym mieście odczyta dekret zabraniający tworzenia zadań związanymi z szachami. Szach chce, żeby goniec odwiedził każde miasto dokładnie raz. Goniec wyjeżdża ze stolicy algocji – miasta x i ma do niej wrócić.
14.	Zaimplementować Dijkstrę
15.	----- || ----- Bellmana forda
16.	Graf z wagami, które są dodatnimi liczbami rzeczywistymi, ale tak by iloczyn wag był minimalny
17.	Wymiana walut, dana jest tabela kursów; dla każdego x,y wpis k[x][y] piszę ile waluty x za jednostkę y; napisać taki algorytm, który sprawdza, czy istnieje taka waluta z, że za jednostkę z można uzyskać więcej niż jednostkę z przez przejście cyklu zmian
18.	Dany jest graf, gdzie każda krawędź ma wagę ze zbioru 1-|E|; wagi są parami różne. Zaproponować algorytm, który dla danych x i y oblicza ścieżkę o najmniejszej sumie wag po krawędziach o malejących wagach, jak nie da się to zwrócić none.
19.	Ania i Bob Jadą z miasta x do miasta y. Dana jest mapa kraju w postaci grafu, gdzie wierzchołki to miasta, a krawędzie to drogi z długościami ważonymi jako liczba naturalna. Ania i bob prowadzą na zmianę zmieniając się w każdym możliwym mieście, Ania wybiera trasę i decyduje kto prowadzi pierwszy. Zaproponować algorytm, który da taką trasę i osobę pierwszą, żeby Ania  przejechała jak najmniej 
20.	Samochód i stacje z bitu, tylko że w baku zamiast 100 litrów jest D
21.	Ważone drzewo, znaleźć wierzchołek, taki że odległość od najdalszego jest najmniejsza
22.	 Dany jest Graf. Jeżeli między wierzchołkami v,u jest ścieżka, jeżeli nie są bezpośrednio połączone to je połączyć (domknięcie przechodnie)
23.	Implementacja Union Find z górnym szacowaniem wysokości drzewa (?)
24.	Znaleźć najmniejszy cykl w grafie skierowanym
25.	Transport Atomowy – dany jest graf, pozycje pierwiastków atomowych, i minimalny dystans między nimi. Zaproponować Algorytm, który rozstrzyga czy da się zamienić pierwiastki miejscami tak, żeby nie wybuchły (opcja alternatywna, graf jest pełny ta zwykła jest „przesadzona” wg falisza, czyli śmierć)
