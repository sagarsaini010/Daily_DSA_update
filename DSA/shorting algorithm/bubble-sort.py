def bubble_sort(arr,n = None):
    if n == None:
        n = len(arr)
    if n == 1:
        return arr
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [6,7,4,5,6,3,2,1]
print(bubble_sort(arr))