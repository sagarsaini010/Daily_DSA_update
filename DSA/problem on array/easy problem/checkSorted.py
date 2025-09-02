def checkSort(arr):
    n =len(arr)
    pointer = arr[0]
    for i in arr:
        if pointer<=i:
            pointer = i
        elif pointer>i:
            return False
    return True



arr= [1,1,2,2,3,4,5,6,6]
ans =checkSort(arr)
print(ans)