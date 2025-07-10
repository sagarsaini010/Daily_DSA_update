def union(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    temp =[]
    i=0
    j=0

    while i<n1 and j < n2:
        if arr1[i] <= arr2[j]:
            if not temp or temp[-1] != arr2[j]:
                temp.append(arr1[i])
            i+=1
        elif arr1[i] >= arr2[j]:
            if not temp or temp[-1] != arr2[j]:
                temp.append(arr2[j])
            j+=1
    while i < n1:
        if not temp or temp[-1] != arr2[j]:
            temp.append(arr1[i])
        i+=1
    while j < n2:
        if not temp or temp[-1] != arr2[j]:
            temp.append(arr2[j])
        j+=1
    return temp


arr1 = [1,2,3,4,5,6]
arr2 = [ 3,4,5,6,7,8,9]

print(union(arr1,arr2))
