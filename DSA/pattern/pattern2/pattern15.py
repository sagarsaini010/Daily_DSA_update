def pattern(n):
    for i in range(n):
        A=65
        for j in range(n-i):
            print(chr(A),end="")
            A=A+1
        print("")
pattern(5)