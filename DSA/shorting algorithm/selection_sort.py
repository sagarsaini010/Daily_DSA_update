def selectionSort(arr):
        #code here
        n = len(arr)
        print(n)
        for i in range(n-1):
            mini = i
            for j in range(i+1,n):
                if arr[j]<arr[mini]:
                    mini = j
            arr[i],arr[mini] = arr[mini],arr[i]
            
            
arr = [2,4,1,78,25]
selectionSort(arr)
print(arr)