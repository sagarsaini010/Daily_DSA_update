def removeDuplicate(arr):
    sett =set()
    for j in arr:
        sett.add(j)

    return sett
arr= [1,2,3,4,5,1]
ans =removeDuplicate(arr)
print(ans)