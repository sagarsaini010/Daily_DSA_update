def apperOnce(arr):
    n = len(arr)
    xor1=0
    for i in range(n):
        xor1 = xor1^arr[i]
    return xor1

arr = [1,1,2,6,5,4,6,5,2]
ans=apperOnce(arr)
print(ans)