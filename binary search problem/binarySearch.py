<<<<<<< HEAD
def binarySearch(arr,k):
    n = len(arr)
    left=0
    right=n-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid]==k:
            return mid
        elif arr[mid] > k:
            right = mid-1
        else:
            left = mid+1
    return -1

arr = [-1,0,3,5,9,12]
ans = binarySearch(arr,13)
=======
def binarySearch(arr,k):
    n = len(arr)
    left=0
    right=n-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid]==k:
            return mid
        elif arr[mid] > k:
            right = mid-1
        else:
            left = mid+1
    return -1

arr = [-1,0,3,5,9,12]
ans = binarySearch(arr,13)
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
print(ans)