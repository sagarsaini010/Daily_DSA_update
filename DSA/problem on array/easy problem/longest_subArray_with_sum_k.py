# def longest_subarray(arr,k):
    # n = len(arr)
    
    # length =0
    # for i in range(n):
    #     sum=0
    #     for j in range(i,n):
    #         sum = sum + arr[j]
    #         if sum == k:
    #             length = max(length,j-i+1)
    # print(length)

def longest_subarray(arr, k):
    preSumDict = {}  # Dictionary to store prefix sum and their earliest occurrences
    sum = 0          # Running sum
    maxlen = 0       # Maximum length of subarray with sum = k
    
    for i in range(len(arr)):
        sum += arr[i]  # Update the running sum
        
        # Check if the running sum itself is equal to k
        if sum == k:
            maxlen = i + 1  # Subarray starts from index 0
        
        # Calculate the remainder (sum - k)
        rem = sum - k
        
        # If 'rem' exists in the dictionary, calculate the length
        if rem in preSumDict:
            lent = i - preSumDict[rem]
            maxlen = max(maxlen, lent)
        
        # Store the current sum in the dictionary if it doesn't already exist
        if sum not in preSumDict:
            preSumDict[sum] = i
    
    return maxlen

# Example usage
arr = [1, 2, 3, 1, 1,0, 1, -1, 1, 2, 1, 3]
result = longest_subarray(arr, 3)
print(result)  # Output: 6

                          



