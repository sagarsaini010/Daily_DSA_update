def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    return arr

arr = [3,4,3,2,1,5,6,4,5,7,0,9,8]

print(insertionSort(arr))
         