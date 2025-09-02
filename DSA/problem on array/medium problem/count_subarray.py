def count_subarray(arr,x):
    count =0
    n =len(arr)
    pre_sum ={}
    pre_sum[0] =1
    sum =0
    for i in range(n):
        sum = sum+ arr[i]
        
        rem = sum-x
        if rem in pre_sum:
            count+= pre_sum[rem]
        pre_sum[sum]= pre_sum.get(sum,0)+1
    return count

  

arr=[3,1,2,4]

ans = count_subarray(arr,6)
print(ans)


# if __name__ == '__main__':
#     arr = [0,0,0,0,0,0,0,0,0,0]
#     k = 0
#     cnt = findAllSubarraysWithGivenSum(arr, k)
#     print("The number of subarrays is:", cnt)
