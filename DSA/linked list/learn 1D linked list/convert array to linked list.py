class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def from_array(self, arr):
        self.head = Node(arr[0])
        temp = self.head
        for i in range(1,len(arr)):
            new_node = Node(arr[i])
            temp.next = new_node
            temp = new_node
    
    def show_linked_list(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


arr = [1,2,3,24,45,"sagar",67,89]

ll = Linkedlist()
ll.from_array(arr)
ll.show_linked_list()
        