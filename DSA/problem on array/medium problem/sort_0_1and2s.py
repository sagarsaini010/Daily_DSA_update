def sort_3numbers(arr):
    n = len(arr)
    mid=0
    low=0
    high = n-1
    while mid<=high:
        if arr[mid] ==0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1
    return arr      

arr=[0,1,2,1,2,0,0,0,2,1,0,1,2,0]
ans=sort_3numbers(arr)
print(ans)