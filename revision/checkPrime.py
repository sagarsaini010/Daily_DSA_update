import math
def check_prime(n):
    if n <=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
        

print(check_prime(12))