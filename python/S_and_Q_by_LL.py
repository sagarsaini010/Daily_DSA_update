class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size+=1
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        pop_item = self.top.data
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self._size-=1
        return pop_item
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data
    def size(self):
        return self._size
    def is_empty(self):
        return self.top is None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self._size = 0
    def __str__(self):
        result = []
        current = self.start
        while current:
            result.append(str(current.data))
            current = current.next
        return "Front -> " + " -> ".join(result) + " <- Rear"
    def push(self,data):
        new_node = Node(data)
        if self.start == None:
            self.start = self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node  # ← This line is missing!

        self._size +=1
    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        pop_item = self.start.data
        temp = self.start
        self.start = self.start.next
        temp.next = None
        self._size -=1
        if self.start is None:
            self.end = None
        return pop_item
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.start.data
    def size(self):
        return self._size
    def is_empty(self):
        return self.start is None
