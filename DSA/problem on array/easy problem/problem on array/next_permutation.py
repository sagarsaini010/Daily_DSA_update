def next_prmutation(arr):
    n = len(arr)
    i = n-2

    while i >=0 and arr[i] >= arr[i+1]:
        i-=1
    if i >=0:
        j =n-1
        while arr[j] <= arr[i]:
            j -=1
        arr[i],arr[j] = arr[j],arr[i]
    arr[i+1:] = reversed(arr[i+1:])
    return arr
        


nums = [3,2,1]
print(next_prmutation(nums))
        