# def sum1(n,sum =0):
#     if n == 0:
#         print(sum)
#         return
#     print(sum)
#     sum1(n-1,sum+n)
#     print(sum)

# sum1(4)
    


def sum1(n):
    if n ==0:
        return 0
    return n + sum1(n-1)

print(sum1(4))