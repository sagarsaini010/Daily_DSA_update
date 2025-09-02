class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def arr2ll(self, arr):
        self.head = Node(arr[0])
        temp = self.head
        for i in range(1,len(arr)):
            new_node = Node(arr[i])
            temp.next = new_node
            temp = new_node

        return self.head
    
    def show_linked_list(self, head):
        temp = head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    
    def insert_at_head(self,head,k):
        new_node = Node(k)
        if not head:
            head = new_node
            return head 
        new_node.next = head
        head = new_node
        return head
    
    def insert_at_tail(self,head,k):
        new_node = Node(k)
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return head
    
    def insert_at_position(self,head,k,position):
        new_node = Node(k)
        if position == 1:
            if not head:
                head = new_node
                return head
            new_node.next = head
            head = new_node
            return head
        cunt =0
        temp = head
        pre = None

        while temp:
            cunt += 1
            if cunt == position:
                pre.next = new_node
                new_node.next = temp
                break
            pre = temp
            temp = temp.next
        if cunt +1 == position:
            pre.next = new_node
        return head
    
    def insert_at_after_el(self,head,k,el):
        new_node = Node(k)
        temp = head
        pre_node = None
        if head.data == el:
            pre_node = temp.next
            temp.next = new_node
            new_node.next = pre_node
            return head
        while temp:
            if temp.data == el:
                temp.next = new_node
                new_node.next = pre_node
                break
            temp = temp.next
            if temp != None:
                pre_node = temp.next
        return head
    
    def insert_at_befor_el(self,head,k,el):
        new_node = Node(k)
        temp = head
        pre = None
        if head.data == el:
            new_node.next = head
            head = new_node
            return head
        while temp:
            if temp.data == el:
                pre.next = new_node
                new_node.next = temp
                break
            pre = temp
            temp = temp.next
        return head




arr = [12,3,4,6,7]

ll = Linkedlist()
head = ll.arr2ll(arr)
ll.show_linked_list(head)

head = ll.insert_at_befor_el(head,26,8)

ll.show_linked_list(head)

