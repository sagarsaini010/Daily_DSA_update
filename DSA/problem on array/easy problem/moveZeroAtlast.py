def moveZeros(arr):
    # n= len(arr)
    # temp = []
    # for i in range(n):
    #     if arr[i]!=0:
    #         temp.append(arr[i])
    # numOfNoneZero = len(temp)
    # for i in range(numOfNoneZero):
    #     arr[i]=temp[i]
    # for i in range(numOfNoneZero,n):
    #     arr[i]=0
    # return arr

    j =-1
    n =len(arr)

    for i in range(n):
        if arr[i]==0:
            j=i
            break

    for i in range(j,n):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr




arr=[1,0,3,0,5,0,7]
ans =moveZeros(arr)
print(ans)
