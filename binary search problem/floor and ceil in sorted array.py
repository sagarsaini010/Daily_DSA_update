<<<<<<< HEAD
def floorAndCeli(arr,k):
    n = len(arr)
    left =0
    right =n-1
    ans1=n
    ans2=-1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] >= k:
            ans1 = arr[mid]
            right = mid-1
        elif arr[mid] <= k:
            ans2 = arr[mid]
            left = mid+1
    return ans2,ans1


arr =[3, 4, 4, 7, 8, 10]

ans = floorAndCeli(arr,2)
=======
def floorAndCeli(arr,k):
    n = len(arr)
    left =0
    right =n-1
    ans1=n
    ans2=-1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] >= k:
            ans1 = arr[mid]
            right = mid-1
        elif arr[mid] <= k:
            ans2 = arr[mid]
            left = mid+1
    return ans2,ans1


arr =[3, 4, 4, 7, 8, 10]

ans = floorAndCeli(arr,2)
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
print(ans)