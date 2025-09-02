def pattern(n):
    for i in range(n):
        if i%2==0:
            k=1
        else:
            k=0
        for j in range(i+1):
            print(k,end="")
            k=1-k
        print("")

pattern(5)