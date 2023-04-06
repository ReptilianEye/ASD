from queue import PriorityQueue


from kol1testy import runtests


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.heap = None
        self.index = None


def print_heaps(left_heap, right_heap):
    print("Stan lewego kopca")
    for i in range(len(left_heap.queue)):
        el = left_heap.queue[i][1]
        print(el.val, el.index)
    # print()
    print("Stan prawego kopca")
    for i in range(len(right_heap.queue)):
        el = right_heap.queue[i][1]
        print(el.val, el.index)
    print()


def prepare_heaps(T):
    h_min_left = PriorityQueue()
    h_max_right = PriorityQueue()
    for i in range(k):
        T[i].heap = "L"
        h_min_left.put(((T[i].val, i), T[i]))

    for i in range(p-k):
        curr = T[k+i]
        if h_min_left.queue[0][1].val < curr.val:
            lower = h_min_left.get()[1]
            T[lower.index].heap = "R"
            T[curr.index].heap = "L"
            h_min_left.put(((curr.val, -curr.index), curr))
            h_max_right.put(((-lower.val, -lower.index), lower))
        else:
            h_max_right.put(((-curr.val, -curr.index), curr))

    return h_min_left, h_max_right


def ksum(T, k, p):
    n = len(T)
    s = 0
    for i in range(n):
        new = Node(T[i])
        new.index = i
        T[i] = new
    mainHeap, pomHeap = prepare_heaps(T)
    n_left = k
    for i in range(p, n-1):
        # print_heaps(mainHeap, pomHeap)

        while not mainHeap.empty() and mainHeap.queue[0][1].index < i-p:
            mainHeap.get()
        # while not pomHeap.empty() and pomHeap.queue[0][1].index < i-p:
        #     pomHeap.get()
        # print(mainHeap.queue[0][1].val)
        s += mainHeap.queue[0][1].val

        deleted = T[i-p]
        if T[deleted.index].heap == "L":
            n_left -= 1

        next = T[i+1]  # i == next.index
        if next.val > pomHeap.queue[0][1].val:
            if n_left < k:
                T[next.index].heap = "L"
                mainHeap.put(((next.val, -next.index), next))
                n_left += 1
            else:
                top_left = mainHeap.queue[0][1]
                if top_left.val < next.val:
                    top_left = mainHeap.get()[1]
                    T[top_left.index].heap = "R"
                    T[next.index].heap = "L"
                    pomHeap.put(
                        ((-top_left.val, -top_left.index), top_left))
                    mainHeap.put(((next.val, -next.index), next))
                else:
                    pomHeap.put(((-next.val, -next.index), next))
                    T[next.index].heap = "R"

        else:
            if n_left < k:
                top_right = pomHeap.get()[1]
                mainHeap.put(((top_right.val, -top_right.index), top_right))
                T[top_right.index].heap = "L"
            pomHeap.put(((-next.val, next.index), next))
            T[next.index].heap = "R"

    return s


# T = [7, 9, 1, 5, 8, 6, 2, 12]
# k = 4
# p = 5

T = [5, 8, 3, 1, 2, 8, 5, 4, 3, 2, 1]
p = 4
k = 2

res = ksum(T, k, p)
print(res)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
