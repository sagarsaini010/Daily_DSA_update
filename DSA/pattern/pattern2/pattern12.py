def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end="")
        for k in range(2*n-2*(i+1)):
            print(" ",end="")
        for m in range(i+1,0,-1):
            print(m,end="")
        print("")
pattern(4)