def gcd(a,b):
    while a>0 and b>0:
        if a>b:
            a = a%b
        else:
            b = b%a
    if a>b:
        return a
    else:
        return b
    

ans= gcd(52,10)
print(ans)