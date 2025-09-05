def secondLargest(arr):
    lrg = -10**9
    slrg = lrg
    n = len(arr)
    for i in range(n):

        if arr[i] > lrg:
            slrg = lrg
            lrg = arr[i]
        elif arr[i] > slrg and arr[i] < lrg:
            slrg = arr[i]
                      
             
    return slrg
    
arr = [99,1,3,523,2,62,8]

print(secondLargest(arr))