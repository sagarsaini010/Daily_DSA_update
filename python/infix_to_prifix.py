from collections import deque
def nextSmallerElements(arr):
    # Your code goes here
    nge=[]
    n = len(arr)
    st = deque()
    for i in range(n,-1,-1):
        while len(st)!=0 and arr[i] <= st[-1]:
            st.pop()
        nge.append(-1 if len(st) == 0 else st[-1])
        st.append(arr[i])

    return list(reversed(nge))




arr = [4, 8, 5, 2, 25]

print(nextSmallerElements(arr))


# class Solution:
#     def leftmax(self,height):
#         n = len(height)
#         prefix=[0]*n
#         prefix[0]= height[0]
#         for i in range(1,n):
#             prefix[i] = max(prefix[i-1],height[i])
#         return prefix
#     def rightmax(self,height):
#         n = len(height)
#         suffix=[0]*n
#         suffix[n-1]= height[n-1]
#         for i in range(n-2,-1,-1):
#             suffix[i] = max(suffix[i+1],height[i])
#         return suffix


#     def trap(self, height: List[int]) -> int:
#         total=0
#         n = len(height)
#         prefixMax = self.leftmax(height)
#         suffixMax = self.rightmax(height)
#         for i in range(n):
#             if height[i] < prefixMax[i] and height[i] < suffixMax[i]:
#                 total += min(prefixMax[i],suffixMax[i])- height[i]
#         return total




# class Solution:
#     def leftmax(self,height):
#         n = len(height)
#         prefix=[0]*n
#         prefix[0]= height[0]
#         for i in range(n):
#             prefix[i] = max(prefix[i-1],prefix[i])
#         return prefix
#     def rightmax(self,height):
#         n = len(height)
#         suffix=[0]*n
#         suffix[n-1]= height[n-1]
#         for i in range(n-2,-1,-1):
#             suffix[i] = max(suffix[i+1],suffix[i])
#         return suffix


#     def trap(self, height: List[int]) -> int:
#         total=0
#         n = len(height)
#         prefixMax = self.leftmax(height)
#         suffixMax = self.rightmax(height)
#         for i in range(n):
#             # if height[i] < prefixMax[i] and 
#             water = min(prefixMax[i],suffixMax[i])- height[i]
#             total+= water if water >= 0 else 0
#         return total
