def armstrong(n):
    num = n
    digit = 0
    while num > 0:
        last_digit = num%10
        num = int(num/10)
        digit= digit+(last_digit*last_digit*last_digit)
    if digit == n:
        return True
    else:
        return False
    

ans = armstrong(1634)
print(ans)