# zadanie polega na napisaniu funkcji ktora w czasie O(E), znajduje najkrótsza ścieżke pomiedzy dwoma wierzchołkami
# rozwiązanie:
# sortujemy wierzchołki topologicznie, a nastepnie przeglądamy je w posortowanym porządku
# ponieważ każdą krawedź przeglądamy dokładnie raz a zwykle E > V złożoność wynosi O(V*E)
