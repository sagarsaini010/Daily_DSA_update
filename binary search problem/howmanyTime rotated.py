<<<<<<< HEAD
def find_rotation(arr):
    n = len(arr)
    low =0
    high = n-1
    while low < high:
        mid = (low + high)//2
        if arr[high] < arr[mid]:
            low = mid + 1
        else:
            high = mid
    return low

arr = [4,5,6,7,0,1,2,3]
ans = find_rotation(arr)
=======
def find_rotation(arr):
    n = len(arr)
    low =0
    high = n-1
    while low < high:
        mid = (low + high)//2
        if arr[high] < arr[mid]:
            low = mid + 1
        else:
            high = mid
    return low

arr = [4,5,6,7,0,1,2,3]
ans = find_rotation(arr)
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
print(ans)