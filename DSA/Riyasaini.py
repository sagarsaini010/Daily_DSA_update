# class Node:
#     def __init__(self,data1,next1 = None):
#         self.data = data1
#         self.next = next1


# x = Node(2)

# y = x

# print(x.data)
# print(y)
# print(x)

class Node:  # Ek coach ka model
    def __init__(self, data):
        self.data = data  # Coach ke andar ka data
        self.next = None  # Agla coach ka link

class LinkedList:  # Poori train ka system
    def __init__(self):
        self.head = None  # Shuruwat me train empty hai

    def append(self, data):
        new_node = Node(data)  # Naya coach banao
        if not self.head:  # Agar train me koi coach nahi hai
            self.head = new_node  # Engine set kar do
            return
        temp = self.head
        while temp.next:  # Aakhri coach tak jao
            temp = temp.next
        temp.next = new_node  # Naya coach attach kar do

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")  # Har coach ka data print
            temp = temp.next
        print("None")  # Train ka end

# 🚀 Example Usage:
ll = LinkedList()
ll.append(1)  # Pehla coach
ll.append(2)  # Doosra coach
ll.append(3)  # Teesra coach
ll.display()  # Train ko dekho
