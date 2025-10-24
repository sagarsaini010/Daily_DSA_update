class Solution:
    def max_sum(self,arr,k):
        n = len(arr)
        i = 0
        j = 0
        sum = 0
        max_sum = -10**9
        while j < n:
            sum = sum+arr[j]
            if j < k-1:
                j+=1
            elif j-i+1 == k:
                max_sum = max(sum,max_sum)
                sum = sum - arr[i]
                i+=1
                j+=1
        return max_sum
                
                
arr = [1,2,3,4,5,6,7,8,9]

sol = Solution()
maxSum = sol.max_sum(arr,3)
print(maxSum)
            