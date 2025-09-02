def lowerBound(arr,k):
    low =0 
    high = len(arr) - 1
    ans = len(arr)
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= k:
            ans = mid
            high = mid -1
        else:
            low = mid + 1
    return ans

def count_ones(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count_max = 0
    index = -1
    for i in range(n):
        count_ones = m - lowerBound(matrix[i],1)
        if count_ones > count_max:
            count_max = count_ones
            index = i
    return index

