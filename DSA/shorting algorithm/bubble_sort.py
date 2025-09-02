# def bubbleShort(arr: list):
#     n = len(arr)
#     for i in range(n-1):
#         print(i)
#         didSwap =0
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j+1],arr[j] = arr[j],arr[j+1]
#                 didSwap = 1
#         if didSwap == 0:
#             break



# arr = [1,2,3,4,5,6]

# bubbleShort(arr)
# print(arr)

def bubbleSort(arr,n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return
    for i in range(n-1):
         if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    bubbleSort(arr,n-1)
    


arr= [3,2,1,2,6,4,7,2,8,5,3,1,9]
bubbleSort(arr)
print(arr)