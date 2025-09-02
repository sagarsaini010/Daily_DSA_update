def rotateArray(arr, k):
    n = len(arr)
    # for i in range(k):
    #     last =arr[n-1]
    #     for j in range(n,0,-1):
    #         arr[j-1] =arr[j-2]
    #     arr[0]=last
    # return arr
    k=k%n
    arr[n-k:] = arr[n-k:][::-1]
    arr[0:n-k] = arr[0:n-k][::-1]
    arr[:]=arr[:][::-1]
    return arr

arr=[1,2,3,4,5,6,7]
ans =rotateArray(arr,3)
print(ans)