def revers_array(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r] = arr[r], arr[l]
    revers_array(arr,l+1,r-1)
    return arr

    





arr = [1,2,3,4,5,6,7]
print(revers_array(arr,0,6))
    