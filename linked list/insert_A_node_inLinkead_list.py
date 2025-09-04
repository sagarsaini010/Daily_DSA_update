from Modules.sLinkedList import LinkedList

ll = LinkedList()
arr = [1,2,3,4,5,6,7]
ll.append(arr,len(arr))
ll.insertAfterElement(4,4)
print(ll)
