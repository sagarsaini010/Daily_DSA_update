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
print(ans)