def intersection(arr1,arr2):
    n =len(arr1)
    m = len(arr2)
    temp=[]
    i , j = 0, 0
    while i < n and j < m:
        if arr1[i] == arr2[j]:
           if len(temp) == 0 or temp[-1] != arr1[i]:
               temp.append(arr1[i])
           i+=1
           j+=1
        elif arr1[i] < arr2[j]:
            i+=1
        elif arr1[i] > arr2[j]:
            j+=1
    return temp      


arr1=[1,1,2,3,4,4,8,9]
arr2=[-8,-7,7,8,9,10]
ans =intersection(arr1,arr2)
print(ans)