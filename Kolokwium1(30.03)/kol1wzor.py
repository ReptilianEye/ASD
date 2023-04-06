from queue import PriorityQueue


from kol1testy import runtests


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

        while not main_heap.empty() and main_heap.queue[0][1].i < i-p:
            main_heap.get()
        while not rest_heap.empty() and rest_heap.queue[0][1].i < i-p:
            rest_heap.get()

        s += main_heap.queue[0][1].val

        deleted = T[i-p]
        if T[deleted.i].heap == "L":
            main_size -= 1

        next = T[i]  # i == next.i

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

    s += main_heap.queue[0][1].val
    return s


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
