def divide(dividend,divisor):
    if dividend == divisor:
        return 1
    sign = True
    if dividend >= 0 and divisor <0:
        sign = False
    if dividend<0 and divisor > 0:
        sign = False
    quotient = 0
    n = dividend
    d = divisor
    while n >=divisor:
        cnt = 0
        while n >= d << cnt+1:
            cnt+=1
        quotient += 1<<cnt
        n-= d << cnt

    return quotient if sign else (-1 * quotient)



ans = divide(22,3)

print(ans)