class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.back = None


class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        return " -> ".join(result) + " -> None"
    def __str_reverse__(self):
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        result = []
        while temp:
            result.append(str(temp.data))
            temp = temp.back
        return " -> ".join(result) + " -> None"
    
    def creat_2dLL(self,arr):
        if not arr:
            print("No value to creat list")
            return
        new_node = Node(arr[0])
        if not self.head:
            self.head = new_node
        temp = self.head
        for i in range(1,len(arr)):
            new_node = Node(arr[i])
            temp.next = new_node
            new_node.back = temp
            temp = new_node
        return self.head
    
    def deletHead(self):
        if not self.head:
            print ("[INFO] List is already empty")
            return
        temp = self.head
        if not temp.next:
            print('[INFO] Now list is empty')
            self.head = None
        else:
            self.head = temp.next
            self.head.back = None

    def deletTail(self):
        if not self.head or not self.head.next:
            self.head = None
            print("list is empty")
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next.back = None
        temp.next = None
    
    def deletValue(self,x):
        if not self.head:
            print("list is empty")
            return
        elif self.head.data == x and not self.head.next:
            self.head = None
            print("Now list is empty")
            return
        if self.head.data ==x:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.head.back = None
            return
        temp = self.head
        while temp:
            if temp.data == x: 
                if temp.next:
                    temp.back.next = temp.next
                    temp.next.back = temp.back
                    temp.back = None
                    temp.next = None
                else:
                    temp.back.next = None
                temp.back = None
                temp.next = None
                return  
                temp = temp.next
    

    def deletIndex(self,x):
        if not self.head:
            print("list is empty")
            return
        if x == 1 and self.head.next == None:
            self.head = None
            print("now list is empty")
            return
        if x == 1 and self.head.next:
            temp = self.head
            self.head = temp.next
            self.head.back = None
            temp.next = None
            return
        temp = self.head
        index = 1
        while temp:
            if index == x:
                if temp.next:
                    temp.back.next = temp.next
                    temp.next.back = temp.back
                else:
                    temp.back.next = None
                temp.back = None
                temp.next =None
                return
            index+=1
            temp = temp.next
        print("[INFO] Index not found")
    
    def insertAtHead(self,x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            print("List is created")
            return 
        temp = self.head
        temp.back = new_node
        new_node.next = temp
        self.head = new_node
    
    def insertAtTail(self,x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            print("list is created")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.back = temp
    def insertAtIndex(self,x,ind):
        new_node = Node(x)
        if ind ==1: 
            if not self.head:
                self.head= new_node
                return
            else:
                temp = self.head
                temp.back = new_node
                new_node.next = temp
                self.head = new_node
                return

        temp = self.head
        index = 1
        while temp and index < ind - 1:
            temp = temp.next
            index += 1

        if not temp:
            print(f"[ERROR] Index {ind} is out of bounds")
            return

        new_node.next = temp.next
        new_node.back = temp

        if temp.next:
            temp.next.back = new_node

        temp.next = new_node

        