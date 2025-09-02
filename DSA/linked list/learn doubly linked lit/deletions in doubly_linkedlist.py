class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def arr2Dll(self, arr):
        self.head = Node(arr[0])
        temp = self.head
        for i in range(1, len(arr)):
            new_node = Node(arr[i])
            temp.next = new_node
            new_node.back = temp
            temp = new_node
        return self.head
    
    def show_linked_list(self, head):
        temp = head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        
        print("None")

    
    def delet_head(self, head):
        if head == None or head.next == None:
            return None
        head = head.next
        head.back = None
        return head
    
    def delet_tail(self, head):
        if head == None or head.next == None:
            return None
        temp = head
        while temp.next.next:
            temp = temp.next
        temp.next.back = None
        temp.next = None
        return head


arr = [1,2,3,4,5,6]
ll = Linkedlist()
head = ll.arr2Dll(arr)
ll.show_linked_list(head)

head = ll.delet_head(head)
ll.show_linked_list(head)

        