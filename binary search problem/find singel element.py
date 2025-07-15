def find_singel_element(arr):
    n = len(arr)
    low =0
    high = n-1
    while low <= high:
        mid = (low + high)// 2
        if n==1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[n-1] != arr[n-2]:
            return arr[n-1]
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid+1]):
            low = mid+1
        else:
            high = mid-1

    return -1

nums = [1,1,2,2,3,3,4,4,8,8]
ans = find_singel_element(nums)
print(ans)