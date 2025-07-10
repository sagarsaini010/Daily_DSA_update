def largest_element(arr):
    n = len(arr)
    largest = arr[0]
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
    print(largest)


arr = [1,2,3,4,5,9,8,65,4,3]
largest_element(arr)