# def sum_find(arr,k):
#     n = len(arr)
#     for i in range(n):
#         sum = arr[i]
#         for j in range(n):
#             if i==j:                        something is wrong    
#                 continue
#             sum = sum+arr[j]
#             if sum ==k:
#                 return i,j
#             else:
#                 sum=0
#     return False

# def sum_find(arr,k):
#     n = len(arr)
#     for i in range(n):
#         sum = arr[i]
#         for j in range(i,n):               better 
#             if i==j:
#                 continue
#             if sum+arr[j]==k:
#                 return i,j
          
#     return False

# def sum_find(arr,k):
#     n = len(arr)
#     dict_check ={}
#     for i in range(n):
#         rem = k-arr[i]                          
#         if rem in dict_check:
#             return i,dict_check[rem]
#         if rem not in dict_check:
#             dict_check[arr[i]]=i
#     return False


def sum_find(arr,k):
    n = len(arr)
    left =0
    right = (n-1)
    while left<right:
        if arr[left]+arr[right] ==k:                   #greedy approach
            return left,right
        elif arr[left]+arr[right]>k:
            right-=1
        else:
            left+=1
    return False



arr=[1,2,3,4,5,8,9]
arr.sort()
ans=sum_find(arr,6)

print(ans)