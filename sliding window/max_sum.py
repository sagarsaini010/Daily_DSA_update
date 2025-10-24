class Solution():
    def max_sum(self,arr,k):
        n = len(arr)
        start = 0 
        sum = 0 
        max_sum = -10**9
        for i in range(n):
            sum = sum + arr[i]
            if i - start + 1 == k:
                max_sum = max(max_sum,sum)
                sum = sum - arr[start]
                start+=1
        return max_sum
        
sol = Solution()
arr = [1,2,3,4,5,6,7,8,9]

maxsum = sol.max_sum(arr,3)
print(maxsum)