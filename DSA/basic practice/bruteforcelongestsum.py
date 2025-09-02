def longestsum(arr,k):
    n = len(arr)
    length=0
    for i in range(n):
        for j in range(i,n):
            sum =0
            for l in range(i,j+1):
                sum+=arr[l]
            if sum ==k:
                length = max(length,j-i+1)
    print(length)


arr = [1, 2, 3, 1, 1,0, 1, -1, 1, 2, 1, 3]
result = longestsum(arr, 3)# Output: 6