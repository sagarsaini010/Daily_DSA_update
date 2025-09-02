import math

def checkprime(n):
    count=0
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i==0):
            count+=1
            if(n/i != i):
                count+=1
    if count == 2:
        return True
    else:
        return False
    

ans = checkprime(11)
print(ans)