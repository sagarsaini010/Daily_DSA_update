def missing(arr):
    n = len(arr)
    sum1 = (n*(n+1))//2
    sum2 = sum(arr)
    return sum1 - sum2

arr =[0,1,2,3,5,6,7,8,9]
print(missing(arr))