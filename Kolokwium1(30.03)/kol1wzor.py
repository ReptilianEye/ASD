from queue import PriorityQueue
from kol1testy import runtests

# Piotr Rzadkowski - napisane po wyjaśnieniu
# Algorytm opiera się na dwóch kopcach (reprezentowanych przez PriorityQueue) - main i rest. W kopcu main (kopiec minimum) trzymamy k najwiekszych liczb w danym
# p-elementowym wycinku. Dzieki temu mamy zawsze dostep do k-tego najwiekszego elementu w czasie O(1), bo jest on korzeniem tego kopca. Pozostałe p-k liczby
# trzymamy w kopcu rest (kopiec maximum)
# W fazie wstępnej bierzemy pierwsze p liczb i tworzymy odpowiednie strukury.
# W każdej kolejnej będziemy usuwali element z którego sie przesuwamy i dodajemy nowy, który aktualnie dochodzi do przedziału
# Odczytywanie k-tej wartości:
# - Odczytanie korzenia main
# Usuwanie:
# - Usuwanie polega tylko na sprawdzeniu w którym kopcu był usuniety element i odpowiednio zmniejszamy liczniki oznaczące wielkości kopców.
# Dodawanie:
# - Na początek sprawdzamy, czy kopiec main jest pełny. Jeśli nie to na pewno będziemy chceli go uzupełnić o jeden element. Będzie to albo element będący w korzeniu kopca rest, albo element który doszedł. Wiekszy z nich trafi do main, a mniejszy do rest.
# Jeśli kopiec main był pełny to na pewno będziemy uzupełniali kopiec rest o jeden element. Do niego chcemy włożyć element mniejszy z pary korzeń main i nowo dodany element.

# Po takich operacjach, możliwa jest sytuacja, że w co najmniej jednym z korzeni kopców jest poza przeszukiwanym podziałem, a to oznacza, że powien zostać usunięty. Czyścimy oba kopce z takich elementów.
#Złożoność tego algorytmu to nlogn bo dla każdego przedziału (których jest w zaokrągleniu n), wstawia element do kopca, co ma złożoność logn (bo w kopcu jest w zaokrągleniu w góre n elementów);

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.heap = None
        self.i = None


def print_heaps(left_heap, right_heap):
    print("Stan lewego kopca")
    for i in range(len(left_heap.queue)):
        el = left_heap.queue[i][1]
        print(el.val, el.i)
    # print()
    print("Stan prawego kopca")
    for i in range(len(right_heap.queue)):
        el = right_heap.queue[i][1]
        print(el.val, el.i)
    print()


def prepare_heaps(T, k, p):
    k_biggest_heap = PriorityQueue()
    rest_heap = PriorityQueue()
    for i in range(k):
        T[i].heap = "L"
        k_biggest_heap.put(((T[i].val, i), T[i]))

    for i in range(p-k):
        curr = T[k+i]
        if k_biggest_heap.queue[0][1].val < curr.val:
            lower = k_biggest_heap.get()[1]
            T[lower.i].heap = "R"
            T[curr.i].heap = "L"
            k_biggest_heap.put(((curr.val, curr.i), curr))
            rest_heap.put(((-lower.val, lower.i), lower))
        else:
            rest_heap.put(((-curr.val, curr.i), curr))

    return k_biggest_heap, rest_heap


def clean(h1, h2, border):
    while not h1.empty() and h1.queue[0][1].i < border:
        h1.get()
    while not h2.empty() and h2.queue[0][1].i < border:
        h2.get()


def add(next, T, main_heap, rest_heap, main_size, k):
    if main_size == k:
        top_main = main_heap.queue[0][1]
        if top_main.val < next.val:
            to_main = main_heap.get()[1]
            to_pom = top_main
            T[next.i].heap = "L"
            main_heap.put(((next.val, next.i), next))
        else:
            to_pom = next
        rest_heap.put(((-to_pom.val, to_pom.i), to_pom))
        T[to_pom.i].heap = "R"

    else:
        if rest_heap.empty():
            to_main = next
        else:
            top_pom = rest_heap.queue[0][1]
            if top_pom.val > next.val:
                rest_heap.get()
                rest_heap.put(((-next.val, next.i), next))
                to_main = top_pom
            else:
                to_main = next
        main_heap.put(((to_main.val, to_main.i), to_main))
        T[to_main.i].heap = "L"
        main_size += 1
    return main_size


def ksum(T, k, p):
    n = len(T)
    s = 0
    for i in range(n):
        new = Node(T[i])
        new.i = i
        T[i] = new

    main_heap, rest_heap = prepare_heaps(T, k, p)
    main_size = k
    for i in range(p, n):
        s += main_heap.queue[0][1].val

        deleted = T[i-p]
        if T[deleted.i].heap == "L":
            main_size -= 1

        next = T[i]
        main_size = add(next, T, main_heap, rest_heap, main_size, k)

        clean(main_heap, rest_heap, i-p+1)
    # endfor

    s += main_heap.queue[0][1].val
    return s


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
