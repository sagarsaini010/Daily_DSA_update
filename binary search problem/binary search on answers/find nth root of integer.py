def fun(mid,n,m):
    ans=1
    for i in range(n):
        ans = ans*mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0


def find_nth_root(n,m):
    low =1
    high = m
    

    while low<=high:
        mid = (low + high) // 2
        midN = fun(mid,n,m)
        if midN == 1:
            return mid
        elif midN == 2:
            high = mid-1
        else:
            low = mid+1
    return -1

ans=find_nth_root(3,27)
print(ans)
