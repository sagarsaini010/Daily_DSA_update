def factorial(n):
    if n == 0:
        return 1
    fact = factorial(n-1)
    sum = fact*n
    return sum
    

print(factorial(5))