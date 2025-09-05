def largest(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(n):
        if arr[i] > temp:
            temp = arr[i]
    return temp

arr = [1,2,9,5,4,6,8,4]

print(largest(arr))
