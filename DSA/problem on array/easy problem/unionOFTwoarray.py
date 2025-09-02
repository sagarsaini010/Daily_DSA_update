def union(arr1,arr2):
    n = len(arr1)
    m =len(arr2)
    # union_set = set()
    # for i in range(n):
    #     union_set.add(a[i])
    # for i in range(m):
    #     union_set.add(b[i])
    # union = sorted(union_set)
    # return union

    temp =[]
    i,j=0,0
    while i<n and j<m:
        if arr1[i] < arr2[j]:
            if len(temp) == 0 or temp[-1] != arr1[i]:
                temp.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            if len(temp) ==0 or temp[-1] != arr2[j]:
                temp.append(arr2[j])
            j+=1
        else:
            if len(temp) == 0 or temp[-1] != arr1[i]:
                temp.append(arr1[i])
            i+=1
            j+=1
    while i<n:
        if len(temp) ==0 or temp[-1] != arr1[i]:
            temp.append(arr1[i])
        i+=1
    while j<m:
        if len(temp) ==0 or temp[-1] != arr2[j]:
            temp.append(arr2[j])
        j+=1
    return temp

        
        


arr1=[1,1,2,3,4,4,8,9]
arr2=[-8,-7,7,8,9,10]
ans =union(arr1,arr2)
print(ans)
