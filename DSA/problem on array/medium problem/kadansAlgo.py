def maxSubArray(nums):
        n =len(nums)
        sum=1
        maxi=-10**4
        for i in range(n):
            sum = sum*nums[i]
            if sum > maxi:
                maxi = sum
            if sum<0:
                sum =0
          
        return maxi

arr = [1,2,-3,0,-4,-5]
ans=maxSubArray(arr)
print(ans)