class Stack:
    def __init__(self,max_size):
        self.stack = []
        self.max_size = max_size

    def push(self,x):
        if self.size() < self.max_size:
            self.stack.append(x)
        else: return "Stack Overflow"

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else: return "Stack is empty"
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack)==0

class Queue:
    def __init__(self,max_size):
        self.queue = []
        self.max_size = max_size

    def push(self,x):
        if self.size() < self.max_size:
            self.queue.append(x)
        else: return "Stack Overflow"

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Stack is empty"
    
    def top(self):
        if not self.is_empty():
            return self.queue[0]
        else: return "Stack is empty"
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue)==0    

s =Queue()
s.push(10)
s.push(30)
s.push(20)
s.push(90)
s.push(100)


print(s.pop())  
