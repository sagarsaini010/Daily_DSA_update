def selection_sort(arr):
    n = len(arr)
    count_comp = 0
    count_swap = 0
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            count_comp +=1
            if arr[j] < arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]
        count_swap+=1
    
    return arr,count_comp,count_swap

            
arr = [2,4,1,78,25,2,4,1,78,25]
tup = selection_sort(arr)
print(tup)        