def find_square_root(n):
    low =1
    high = n
    ans =1
    while low <= high:
        mid =(low + high)//2
        if mid*mid <= n:
            ans = mid
            low = mid+1
        else:
            high = mid -1
    print(ans)

find_square_root(36)

