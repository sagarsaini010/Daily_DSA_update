def longSubarray_sum(arr,k):
    preSumMap = {}
    n = len(arr)
    sum=0
    maxLen=0
    
    for i in range(n):
        sum = sum+arr[i]
        if sum == k:
            maxLen = i+1
        
        preSum = sum-k
        
        if preSum in preSumMap:
            maxLen =max(maxLen,i - preSumMap[preSum])
        if sum not in preSumMap:
            preSumMap[sum] = i
    return maxLen

arr = [2,0,0,3]

print(longSubarray_sum(arr,3))