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
    
    def show_from_back(self, head):
        temp = head
        while temp.next:
            temp = temp.next
        
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.back
        print("None")
    @staticmethod
    def swap(a,b):
        a,b = b,a


    
    def revers_D_ll(self, head):
        temp = head
        while temp:
            # Swap next and back pointers
            temp.next, temp.back = temp.back, temp.next
            # Move backward (which was originally moving forward)
            head = temp
            temp = temp.back  # Because we've swapped, `back` now leads to the next node
        return head



arr = [1,2,3,4,5,6]

ll = Linkedlist()
head = ll.arr2Dll(arr)

ll.show_linked_list(head)

head = ll.revers_D_ll(head)

ll.show_linked_list(head)