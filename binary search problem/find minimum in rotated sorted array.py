def find_minimum(arr):
    n = len(arr)
    low = 0
    high = n-1

    while low < high:
        mid = (low+high)//2

        if arr[mid] > arr[high]:
            low = mid+1
        else:
            high = mid
    return arr[low]



arr =[4,5,6,7,0,1,2]
ans = find_minimum(arr)
print(ans)


# def find_minimum(arr):
#     n = len(arr)
#     low, high = 0, n - 1
    
#     while low < high:
#         mid = (low + high) // 2
        
#         # If mid element is greater than the last element, minimum is on the right half
#         if arr[mid] > arr[high]:
#             low = mid + 1
#         else:
#             high = mid  # Move towards the smaller half
    
#     return arr[low]  # The lowest element is found here

# arr = [4, 5, 6, 7, 0, 1, 2]
# ans = find_minimum(arr)
# print(ans)  # Output: 0