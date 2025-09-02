def count_more_then_half(arr):
    count=0
    count1=0
    n =len(arr)
    for i in range(n):
        if count==0:
            count+=1
            el= arr[i]
        elif arr[i] ==el:
            count+=1
        elif arr[i] != el:
            count-=1
    for i in range(n):
        if arr[i]==el:
            count1+=1
        if count1 > int(n/2):
            return el
    return -1



arr = [2,2,3,4,5,6,2,2,2,2,2,2,2,2,2,21,1,1,1]
ans = count_more_then_half(arr)
print(ans)