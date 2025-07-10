def longest_subArray(arr,k):
    n = len(arr)
    sum =arr[0]
    max_len =0
    # preSumMap = {}

    # for i in range(n):
    #     sum = sum+arr[i]
    #     if sum == k:
    #         max_len = max(max_len,i+1)
        
    #     rem = sum -k
    #     if rem in preSumMap:
    #         length = i - preSumMap[rem]
    #         max_len = max(max_len,length)
        

    #     if sum not in preSumMap:
    #         preSumMap[sum] = i
    right =0
    left = 0
    while right < n:
        while left <= right and sum > k:
            sum -= arr[left]
            left+=1
        if sum == k:
            max_len = max(max_len , right - left + 1)
        
        right+=1
        if right < n:
            sum += arr[right]
    

    return max_len


arr = [2,0,0,3]
result = longest_subArray(arr, 3)
print(result) 
        
