def printname(i,n):
    if i > n:
        return
    print("Sagar saini")
    printname(i+1,n)

printname(1,5)