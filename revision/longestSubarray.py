def longest_subarray(arr = [-1, 1, 1], k = 1
):
    sum =0
    lent = 0
    left = 0
    for right in range(len(arr)):
        sum = sum+arr[right]
        while sum > k:
            sum-= arr[left]
            left+=1
        if sum ==k:
            lent = max(lent,(right-left)+1)
    return lent      

print(longest_subarray())