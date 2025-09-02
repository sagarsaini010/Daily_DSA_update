class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,arr,n):
        for i in range(n):
            new_node = Node(arr[i])
            if not self.head:
                self.head = new_node
                temp = self.head
            else:
                temp.next = new_node
                temp = temp.next
        return self.head
    
    def __str__(self):
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        return " -> ".join(result) + " -> None"

    def insertNodeAtHead(self,x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp

    def insertNodeAtEnd(self,x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insertBeforeElement(self,x,y = None):
        new_node = Node(x)
        if not self.head:
            print("List is empty. Inserting at head")
            self.head = new_node
            return        
        if y == self.head.data:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            if temp.next.data == y:
                new_node.next = temp.next
                temp.next = new_node
                return
            else:
                temp = temp.next
        print(f"Element {y} Not found")    

    def insertAfterElement(self,x,y=None):
        if y is None:
            print("Target element 'y' must be provided")
            return
        if not self.head:
            print("List is empty. Inserting at head.")
            self.head = Node(x)
            return
        new_node = Node(x)
        temp = self.head
        while temp:
            if temp.data == y:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print(f"Element {y} not found")

    def deletNode(self,y):
        
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        if temp.data == y:
            self.head = temp.next
            return
        pre = temp
        temp = temp.next
        while temp:
            if temp.data ==y:
                pre.next = temp.next
                return
            pre = temp
            temp = temp.next

        print(f"Element {y} Not found")
    def search(self,y):
        temp = self.head
        index =0
        while temp:
            if temp.data == y:
                return index
            temp = temp.next
            index+=1
        return -1