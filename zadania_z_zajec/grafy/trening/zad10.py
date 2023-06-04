# zadanie polega na sprawdzeniu w grafie skierowanym czy istnieje taki wierzolek z ktorego istnieje sciezka do każdego innego. Rozszerzeniem tego zadania jest znalezenie każdego takiego

# algorym: pierwszym krokiem jest podzial grafu na silnie spojne skladowe. Dzieki temu dostanimy graf DAG. Dzieki temu mozemy go posortować topologicznie. Kiedy go posortujemy topologicznie to jesli można dojść z pierwszej silnie spojnej skladowej do kazdej innej spojnej skladowej to znaczy, że istnieje taki wierzcholek i są to wszystkie które należą do tej silnie spójnej składowej


#implementacja w pliku dobry_poczatek.py