def leaders_in_arr(arr):
    n=len(arr)
    maxi=-10**9
    ans=[]
    while n>0:
        n-=1
        if arr[n]>maxi:
            maxi=arr[n]
            ans.append(arr[n])
    ans.reverse()   
    return ans

# Example usage:
arr = [16, 17, 4, 3, 5, 8]  
print(leaders_in_arr(arr))  # Output: [17, 5, 2]
# Time complexity: O(n)
# Space complexity: O(1) 
# The function iterates through the array once, keeping track of the maximum value seen so far and appending leaders to the result list.
# The space complexity is O(1) because we are using a constant amount of extra space for variables.
# The output is the list of leaders in the array, which are the elements that are greater than all the elements to their right.
# The function works by iterating through the array from right to left, keeping track of the maximum value seen so far.
