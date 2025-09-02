def fib(n):
    if n<=1:
        return n
    last = fib(n-1)
    slast = fib(n-2)
    return last+slast
print(fib(6))