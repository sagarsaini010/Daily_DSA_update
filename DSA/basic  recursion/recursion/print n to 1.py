def printrevers(i,n):
    if n==i:
        return
    print(n)
    printrevers(i,n-1)

printrevers(0,10)