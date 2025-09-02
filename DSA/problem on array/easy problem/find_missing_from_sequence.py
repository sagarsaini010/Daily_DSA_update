def find_missing(arr):
    n =len(arr)
    hasing_arr=[0]*(n+2)
    print(hasing_arr)
    for i in range(n):
        hasing_arr[arr[i]] = 1
    for i in range(1,len(hasing_arr)):
        if hasing_arr[i]==0:
            return i
        


arr=[1,2,3,4,5,7,8,9]
ans = find_missing(arr)
print(ans)

