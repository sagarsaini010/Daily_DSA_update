def selection_sort(arr,n):
    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini] ,arr[i]
    return arr

arr = [6,7,4,5,6,3,2,1]
print(selection_sort(arr,8))


            