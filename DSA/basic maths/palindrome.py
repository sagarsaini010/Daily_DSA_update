def palindrom(n):
    pali_num =0
    num = n
    while num > 0:
        last_digit = num%10
        num = int(num/10)
        pali_num = pali_num*10+last_digit
    if pali_num == n:
        return True
    else:
        return False




ans = palindrom(1222121)
print(ans)