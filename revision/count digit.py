import math
def count_digit(n):
    count = 0
    # while n >0:
    #     count +=1
    #     n = n//10
    # return count
    
    #taking log base 10 is the optimal way to find no of digit in a number;
    count = int(math.log10(n)+1)
    return count
print(count_digit(10**1000))