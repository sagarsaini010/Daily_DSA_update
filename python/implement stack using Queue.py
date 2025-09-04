from S_and_Q_by_LL import Queue,Stack


class ST:
    def __init__(self):
        self.q = Queue()

    def push(self,x):
        s = self.q.size()
        self.q.push(x)
        for _ in range(s):
            self.q.push(self.q.peek())
            self.q.pop()

    def pop(self):
        if self.q.is_empty():
            raise IndexError("Stack is empty")
        self.q.pop()
    def top(self):
        if self.q.is_empty():
            raise IndexError("Stack is empty")
        return self.q.peek()
    def is_empty(self):
        return self.q.is_empty()
    def size(self):
        return self.q.size()


class Qu:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    def push(self,x):
        while (self.s1.size()):
            self.s2.push(self.s1.peek())
            self.s1.pop()
        self.s1.push(x)
        while(self.s2.size()):
            self.s1.push(self.s2.peek())
            self.s2.pop()
    def pop(self):
        if self.s1.is_empty():
            raise IndexError("Queue is empty")
        self.s1.pop()
    def top(self):
       if self.s1.is_empty():
           raise IndexError("Queue is empty")
       return self.s1.peek()
    
    def size(self):
        return self.s1.size()
    def is_empty(self):
        return self.s1.is_empty()
    

# Stack using Queue
st = ST()
st.push(10)
st.push(20)
st.push(30)
print(st.top())  # Output: 30
st.pop()
print(st.top())  # Output: 20

# Queue using Stack
q = Qu()
q.push(100)
q.push(200)
q.push(300)
print(q.top())  # Output: 100
q.pop()
print(q.top())  # Output: 200