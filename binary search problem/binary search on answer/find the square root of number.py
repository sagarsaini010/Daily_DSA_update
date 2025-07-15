def find_square_root(number):
    low= 0
    high = number
    while low <= high:
        mid = (low+high)//2
        if mid*mid <= number:
            ans = mid
            low = mid+1
        elif mid*mid > number:
            high = mid-1
    return ans
    


print(find_square_root(144))