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
            temp.next = new_node
            temp = temp.next
        return self.head
    
    def showLinkedList(self,head):
        temp = head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")


ll = LinkedList()
arr = [8,7,6,5,4,3,2,1]
head = ll.append(arr,len(arr))
ll.showLinkedList(head)
