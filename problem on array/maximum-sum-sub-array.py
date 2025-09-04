<<<<<<< HEAD
def maximum_sum(arr):
    sum =0
    n= len(arr)
    maxi = -10**9
    start = 0
    end =0
    temp_start =0

    for i in range(n):
        sum = sum + arr[i]
        if sum > maxi:
            maxi = sum
            start = temp_start
            end =i
        if sum < 0:
            sum =0
            temp_start =i+1
    print ( start,end)
    return maxi

nums = [-2,1,-3,4,-1,2,1,-5,-2,1,3,1]
=======
def maximum_sum(arr):
    sum =0
    n= len(arr)
    maxi = -10**9
    start = 0
    end =0
    temp_start =0

    for i in range(n):
        sum = sum + arr[i]
        if sum > maxi:
            maxi = sum
            start = temp_start
            end =i
        if sum < 0:
            sum =0
            temp_start =i+1
    print ( start,end)
    return maxi

nums = [-2,1,-3,4,-1,2,1,-5,-2,1,3,1]
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
print(maximum_sum(nums))