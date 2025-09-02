def count_inversion(arr):
    n = len(arr)
    count =0

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                count+=1
    return count

arr = [5,3,2,3,4]
ans = count_inversion(arr)
print(ans)