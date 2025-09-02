def check_sorted(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False       
    return True
        

arr = [3,3,1,2,3,3,4,5,9,65]
print(check_sorted(arr))