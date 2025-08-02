class Stack:
    def __init__(self,max_size):
        self.stack = [None]*max_size
        self.top = -1
    def push(self,x):
        if self.top >= len(self.stack) - 1:
            raise IndexError("Stack Overflow")
        self.top +=1
        self.stack[self.top] = x
    def pop(self):
        if self.top == -1:
            raise IndexError("Stack Underflow")
        pop_item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -=1
        return pop_item
    def peek(self):
        if self.top == -1:
            raise IndexError("Stack is empty")
        return self.stack[self.top]
    def is_empty(self):
        return True if self.top == -1 else False
    def size(self):
        return self.top+1
    
class Queue:
    def __init__(self,max_size):
        self.queue = [None]*max_size
        self.start=-1
        self.end = -1
        self.size =0

    def push(self,x):
        if self.size >= len(self.queue):
            raise IndexError("Queue Overflow")
        if self.size ==0:
            self.start = 0
            self.end = 0
        else: self.end = (self.end+1)% len(self.queue)
        self.queue[self.end]  = x
        self.size+=1
    
    def pop(self):
        if self.size ==0:
            raise IndexError('Queue Underflow')
        pop_item = self.queue[self.start] 
        self.queue[self.start] = None
        if self.size == 1:
            self.start =-1
            self.end=-1
        else:
            self.start = (self.start+1) % len(self.queue)
        self.size -= 1
        return pop_item
    def peek(self):
        if self.size==0:
            raise IndexError('Queue is empty')
        return self.queue[self.start]
    def get_size(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    

    
        
