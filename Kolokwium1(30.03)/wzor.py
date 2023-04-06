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
    h_min_left = PriorityQueue()
    h_max_right = PriorityQueue()
    for i in range(k):
        T[i].heap = "L"
        h_min_left.put(((T[i].val, i), T[i]))

    for i in range(p-k):
        curr = T[k+i]
        if h_min_left.queue[0][1].val < curr.val:
            lower = h_min_left.get()[1]
            T[lower.i].heap = "R"
            T[curr.i].heap = "L"
            h_min_left.put(((curr.val, curr.i), curr))
            h_max_right.put(((-lower.val, lower.i), lower))
        else:
            h_max_right.put(((-curr.val, curr.i), curr))

    return h_min_left, h_max_right


def ksum(T, k, p):
    n = len(T)
    s = 0
    for i in range(n):
        new = Node(T[i])
        new.i = i
        T[i] = new
    mainHeap, pomHeap = prepare_heaps(T, k, p)
    main_size = k
    for i in range(p, n):
        # print_heaps(mainHeap, pomHeap)

        while not mainHeap.empty() and mainHeap.queue[0][1].i < i-p:
            mainHeap.get()
        while not pomHeap.empty() and pomHeap.queue[0][1].i < i-p:
            pomHeap.get()
        # print(mainHeap.queue[0][1].val)
        s += mainHeap.queue[0][1].val

        deleted = T[i-p]
        if T[deleted.i].heap == "L":
            main_size -= 1
        if deleted == mainHeap.queue[0][1]:
            mainHeap.get()
        if deleted == pomHeap.queue[0][1]:
            pomHeap.get()

        next = T[i]  # i == next.i

        if main_size == k:
            top_main = mainHeap.queue[0][1]
            if top_main.val < next.val:
                to_main = mainHeap.get()[1]
                to_pom = top_main
                T[next.i].heap = "L"
                mainHeap.put(((next.val, next.i), next))
            else:
                to_pom = next
            pomHeap.put(((-to_pom.val, to_pom.i), to_pom))
            T[to_pom.i].heap = "R"

        else:
            if pomHeap.empty():
                to_main = next
            else:
                top_pom = pomHeap.queue[0][1]
                if top_pom.val > next.val:
                    pomHeap.get()
                    pomHeap.put(((-next.val, next.i), next))
                    to_main = top_pom
                else:
                    to_main = next
            mainHeap.put(((to_main.val, to_main.i), to_main))
            T[to_main.i].heap = "L"
            main_size += 1

    s += mainHeap.queue[0][1].val
    return s


# T = [7, 9, 1, 5, 8, 6, 2, 12]
# k = 4
# p = 5

# T = [5, 8, 3, 1, 2, 8, 5, 4, 3, 2, 1]
# p = 4
# k = 2

# T = [51, 56, 45, 6, 75, 52, 49, 58, 71, 36]
# k = 2
# p = 4
# res = ksum(T, k, p)
# print(res)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
