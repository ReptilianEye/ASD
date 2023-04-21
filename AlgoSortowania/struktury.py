class Stack:
    def __init__(self) -> None:
        self.__list = []

    def push(self, x):
        self.__list.append(x)

    def empty(self):
        return len(self.__list) == 0

    def top(self):
        if not self.empty():
            return self.__list[len(self.__list)-1]

    def pop(self):
        if not self.empty():
            return self.__list.pop()


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
