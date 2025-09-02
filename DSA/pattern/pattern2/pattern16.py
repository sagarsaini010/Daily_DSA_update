def pattern(n):
    A = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(A),end=" ")
        A = A+1
        print("")
pattern(5)
        