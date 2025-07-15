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
print(ans)