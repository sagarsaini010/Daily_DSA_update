<<<<<<< HEAD
def set_lowerBound(arr,k):
    left =0
    n = len(arr)
    right = n-1
    ans=n
    while left <= right:
        mid = (left+right)//2
        if arr[mid] >= k:
            ans = mid
            right = mid-1
        else:
            left = mid+1

    return arr[ans]

arr = [3,5,8,15,19]

ans = set_lowerBound(arr,14)
=======
def set_lowerBound(arr,k):
    left =0
    n = len(arr)
    right = n-1
    ans=n
    while left <= right:
        mid = (left+right)//2
        if arr[mid] >= k:
            ans = mid
            right = mid-1
        else:
            left = mid+1

    return arr[ans]

arr = [3,5,8,15,19]

ans = set_lowerBound(arr,14)
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
print(ans)