<<<<<<< HEAD
def setUpperBound(arr,k):
    n = len(arr)
    left =0
    right = n-1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= k:
            ans = mid
            left = mid+1
        else:
            right = mid-1
    return ans


arr = [3,5,8,9,15,19]
ans = setUpperBound(arr,14)              
=======
def setUpperBound(arr,k):
    n = len(arr)
    left =0
    right = n-1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= k:
            ans = mid
            left = mid+1
        else:
            right = mid-1
    return ans


arr = [3,5,8,9,15,19]
ans = setUpperBound(arr,14)              
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
print(ans)