<<<<<<< HEAD
def missing(arr):
    n = len(arr)
    sum1 = (n*(n+1))//2
    sum2 = sum(arr)
    return sum1 - sum2

arr =[0,1,2,3,5,6,7,8,9]
=======
def missing(arr):
    n = len(arr)
    sum1 = (n*(n+1))//2
    sum2 = sum(arr)
    return sum1 - sum2

arr =[0,1,2,3,5,6,7,8,9]
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
print(missing(arr))