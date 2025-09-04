def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]
    return arr

arr = [ 5,4,6,3,7,2,1]

print(selectionSort(arr))