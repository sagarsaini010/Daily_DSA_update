def pattern(n):
    for i in range(n):
        num=n-1-i
        for j in range(i+1):
            print(chr(65+num),end="")
            num+=1
        print("")
pattern(5)