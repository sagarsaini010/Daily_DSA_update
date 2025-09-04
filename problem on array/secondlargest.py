<<<<<<< HEAD
def second_largest(arr):
    n = len(arr)
    largest = arr[0]
    slargest = arr[0]

    for i in range(n):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i]> slargest:
            slargest = arr[i]
    print(slargest)

arr = [10,2,3,4,5,9,8,65,4,3,11]
second_largest(arr)
=======
def second_largest(arr):
    n = len(arr)
    largest = arr[0]
    slargest = arr[0]

    for i in range(n):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i]> slargest:
            slargest = arr[i]
    print(slargest)

arr = [10,2,3,4,5,9,8,65,4,3,11]
second_largest(arr)
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
