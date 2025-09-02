def quick_sort(arr, low, high):
    if low < high:
        pindex = partition(arr, low, high)
        quick_sort(arr, low, pindex - 1)
        quick_sort(arr, pindex + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


array = [5, 3, 8, 6, 2]
print("Original array:", array)
quick_sort(array, 0, len(array)-1)
print("Sorted array:", array)