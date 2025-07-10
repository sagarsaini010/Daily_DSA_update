def consu_pos_nig(arr):
    n = len(arr)
    j =0
    for i in range(n):
        if i%2 == 0 and arr[i] < 0:
            j = i+1
            while j<n:
                if arr[j] < 0:
                    j+=1
                else:
                    break
            arr[i],arr[j]= arr[j],arr[i]
        if i%2 == 1 and arr[i] > 0:
            j = i+1
            while j < n:
                if arr[j] > 0:
                    j+=1
                else:
                    break
            arr[i],arr[j] = arr[j],arr[i]
        return arr
        

    

nums = [-1,1]
print(consu_pos_nig(nums))