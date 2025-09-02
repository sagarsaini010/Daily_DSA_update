def  pattern(n):

    for i in range(n):
        A = 65
        for j in range(n-(i+1)):
            print(" ",end="")
        for k in range(i+1):
            print(chr(A),end="")
            A += 1 
        for l in range(i):
            print((chr(A-2)),end="")
            A = A-1
        print("")
pattern(4)