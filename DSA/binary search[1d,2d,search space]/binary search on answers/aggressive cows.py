def aggressive_cow(arr,k):
    sorted(arr)
    n = len(arr)
    low = 0
    high = arr[n-1]-arr[0]
    ans = -1
    def canWePlace(arr,mid_distance,k):
        count_cows =1
        last = arr[0]
        for i in arr:
            if i - last >= mid_distance:
                count_cows+=1
                last = i
            if count_cows >= k:
                return True
        return False




    while low<=high:
        mid = (low+high)//2
        if canWePlace(arr,mid,k):
            ans = mid
            low = mid+1
        else:
            high = mid-1

    return ans


N = 6
k = 4
arr = [0,3,4,7,10,9]

print(aggressive_cow(arr,k))