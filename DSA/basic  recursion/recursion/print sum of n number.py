def print_sum(i,sum):
    if i<1:
        print(sum)
        return
    print_sum(i-1,sum+i)
print_sum(5,0)