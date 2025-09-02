def reversnum(n):
    rev = 0
    while n>0:
        last_digit= n%10
        n= int(n/10)
        rev = (rev*10)+last_digit
    return rev



num =reversnum(43210000)
print(num)