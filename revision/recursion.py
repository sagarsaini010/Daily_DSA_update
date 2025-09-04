def revers_array(arr,l=None,r=None):
    if l == None:
        l=0
    if r == None:
        r = len(arr)-1
    if l >= r:
        return     
    arr[l],arr[r] = arr[r],arr[l]
    revers_array(arr,l+1,r-1)
    
arr = [ 1,2,3,4,5,6,7]
revers_array(arr)
print(arr)