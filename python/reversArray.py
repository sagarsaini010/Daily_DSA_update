def revers(arr, l = 0, r = None):
    if r == None:
        r= len(arr)-1
    if l >=r:
        return
    arr[l],arr[r] = arr[r],arr[l]
    revers(arr,l+1,r-1)


arr = [1,2,3,4,5,6,7]
revers(arr)
print(arr)