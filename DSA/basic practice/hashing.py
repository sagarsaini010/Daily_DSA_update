# def sort(arr):
#     n = len(arr)  # Get the length of the array
#     low = 0  # Initialize the low pointer
#     mid = 0  # Initialize the mid pointer
#     high = n - 1  # Initialize the high pointer
#     for i in range(n):
#         if arr[mid] == 0:
#             arr[low], arr[mid] = arr[mid], arr[low]
#             low += 1
#             mid += 1
#         elif arr[mid] == 1:
#             mid += 1
#         else:
#             arr[mid], arr[high] = arr[high], arr[mid]
#             high -= 1     
#     return arr

# # Example usage 
# arr = [0, 1, 2, 0, 1, 2, 0, 1, 2]
# result = sort(arr)
# print(result)  # Output: [0, 0, 0, 1, 1, 1, 2, 2, 2]


# def rearrange(arr):
#     n = len(arr)
#     positive_arr = []
#     negative_arr = []
#     for i in range(n):
#         if arr[i] < 0:
#             negative_arr.append(arr[i])
#         else:
#             positive_arr.append(arr[i])
#     for i in range(int(n/2)):
#         arr[i*2] = positive_arr[i]
#         arr[i*2+1] = negative_arr[i]
#     return arr

# # Example usage 
# arr = [1, 2, -3, -4, 5, -6]
# result = rearrange(arr)
# print(result)  # Output: [1, -3, 2, -4, 5, -6]


def rearrange(arr):
    n= len(arr)
    new_arr=[0]*n
    positive =0
    negative =1
    for i in range(n):
        if arr[i]<0:
            new_arr[negative]=arr[i]
            negative +=2
        elif arr[i]>0:
            new_arr[positive]=arr[i]
            positive+=2
    return new_arr

# Example usage 
arr = [1, 2, -3, -4, 5, -6]
result = rearrange(arr)
print(result)  # Output: [1, -3, 2, -4, 5, -6]
