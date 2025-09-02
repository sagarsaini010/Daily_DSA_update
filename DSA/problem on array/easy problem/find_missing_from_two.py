def find_missing(arr):
    n = len(arr)
    count=0
    for i in range(n):
        num=arr[i]
        for i in range(n):
            if arr[i]==num:
                count+=1
        if count==1:
            print(num)
        else:
            count=0
arr=[1,1,2,2,3,4,4]
find_missing(arr)

