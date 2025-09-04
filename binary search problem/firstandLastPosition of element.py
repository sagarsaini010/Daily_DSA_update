<<<<<<< HEAD
def firstAndLastPosition(arr,k):
    n = len(arr)
    left =0
    right =n-1
    ans1=-1
    ans2=n

    while left <= right:
        mid = (left+right)//2
        if arr[mid] <= k:
            if arr[mid]==k:
                ans1=mid
            left = mid+1
        elif arr[mid] >= k:
            if arr[mid]==k:
                ans2=mid
            right = mid-1
    return ans1,ans2


nums = [5,7,7,8,8,10]

ans = firstAndLastPosition(nums,8)
=======
def firstAndLastPosition(arr,k):
    n = len(arr)
    left =0
    right =n-1
    ans1=-1
    ans2=n

    while left <= right:
        mid = (left+right)//2
        if arr[mid] <= k:
            if arr[mid]==k:
                ans1=mid
            left = mid+1
        elif arr[mid] >= k:
            if arr[mid]==k:
                ans2=mid
            right = mid-1
    return ans1,ans2


nums = [5,7,7,8,8,10]

ans = firstAndLastPosition(nums,8)
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
print(ans)