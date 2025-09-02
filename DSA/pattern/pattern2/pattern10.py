def pattern(n):
    for i in range(2*n-1):
        if i>=n:
            for k in range(2*n-(i+1)):
                print("*",end="")
            print("")
        else:
            for j in range(i+1):
               print("*",end="")
            print("")
        
pattern(5)