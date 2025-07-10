def remove_duplicate(arr):
    n = len(arr)
    # seet = set()
    # for j in arr:
    #     seet.add(j)
    # print(seet)
    j =0
    for i in range(n):
        if arr[i] != arr[j]:
            j+=1
            arr[j] = arr[i]
    for k in range(j+1):
        print(arr[k])





arr = [1,1,1,2,2,3,3,3,3,4,5,6,7,8,8,8,9,9,9,9]
remove_duplicate(arr)