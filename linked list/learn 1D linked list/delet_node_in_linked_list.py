class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def convert_arr2ll(self,arr):
        self.head = Node(arr[0])
        temp = self.head

        for i in range(1,len(arr)):
            new_node = Node(arr[i])
            temp.next = new_node
            temp = new_node
        return self.head
        
    def show_linked_list(self,head):
        temp = head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def removeHead(self, head):
        if not head:
            return head
        head = head.next
        return head
    def removeTail(self,head):
        temp = head
        if temp == None or temp.next == None:
            head = None
            return head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
        return head
    
    def remove_Kth_element(self,head,k):
        if head == None:
            return head
        if k == 1:
            head = head.next
            return head
        
        cunt = 0
        temp = head
        pre = None

        while temp:
            cunt+=1
            if cunt == k:
                pre.next = pre.next.next
                break
            pre = temp
            temp = temp.next
        return head
    
    def deletEl(self, head, el):
        if not head:
            return head
        if head.data == el:
            head = head.next
            return head
        temp = head
        pre = None

        while temp:
            if temp.data == el:
                pre.next = pre.next.next
            pre = temp
            temp = temp.next
        return head

            
        

arr = [1,2,3,24,45,"sagar",67,89]

ll = Linkedlist()
head = ll.convert_arr2ll(arr)
ll.show_linked_list(head)


# head = ll.removeHead(head)
# ll.show_linked_list(head)


# head = ll.removeTail(head)
# ll.show_linked_list(head)

# head = ll.remove_Kth_element(head,2)
# ll.show_linked_list(head)

head = ll.deletEl(head, 89)
ll.show_linked_list(head)